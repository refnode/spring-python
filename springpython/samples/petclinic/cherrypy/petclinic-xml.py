"""
   Copyright 2006-2008 SpringSource (http://springsource.com), All Rights Reserved

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.       
"""

import cherrypy
import logging
import os
import noxml
from springpython.context import XmlApplicationContext
from springpython.security.cherrypy31 import AuthenticationFilter, ContextSessionFilter, SecurityFilter
from springpython.security.context import SecurityContextHolder

if __name__ == '__main__':
    """This allows the script to be run as a tiny webserver, allowing quick testing and development.
    For more scalable performance, integration with Apache web server would be a good choice."""

    logger = logging.getLogger("springpython")
    loggingLevel = logging.DEBUG
    logger.setLevel(loggingLevel)
    ch = logging.StreamHandler()
    ch.setLevel(loggingLevel)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") 
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # This sample loads the IoC container from an XML file. The XML-based application context
    # automatically resolves all dependencies and order of instantiation for you. 

    applicationContext = XmlApplicationContext(configLocation = "applicationContext.xml")

    SecurityContextHolder.setStrategy(SecurityContextHolder.MODE_GLOBAL)
    SecurityContextHolder.getContext()
    
    def filter_chainer(filters):
        for f in filters:
            f.run()
    
    def make_session_filter():
        contextSessionFilter = ContextSessionFilter()
        cherrypy.tools.sessionFilter = cherrypy.Tool('before_handler', filter_chainer, priority=74)
        return contextSessionFilter
    
    def make_authentication_filter(manager):
        authFilter = AuthenticationFilter(authManager=manager)
        cherrypy.tools.authFilter = cherrypy.Tool('before_handler', filter_chainer, priority=75)
        return authFilter

    def make_security_filter(manager):
        securityFilter = SecurityFilter(authManager=manager, redirectPath="/login")
        cherrypy.tools.securityFilter = cherrypy.Tool('before_handler', filter_chainer, priority=75)
        return securityFilter
    
    manager = applicationContext.getComponent("authenticationManager")
    accessDecisionManager = applicationContext.getComponent("accessDecisionManager")
    objectDefinitionSource = [
                             ("/vets.*", ["VET_ANY"]),
                             ("/editOwner.*", ["VET_ANY", "OWNER"]),
                             ("/.*", ["VET_ANY", "CUSTOMER_ANY"])
                             ]
    
    session_filter = make_session_filter()
    auth_filter = make_authentication_filter(manager)
    security_filter = make_security_filter(manager)

    conf = {'/': {'tools.sessions.on': True,
                  'tools.sessionFilter.on': True,
                  'tools.sessionFilter.filters': [session_filter, security_filter],
                  "tools.staticdir.root": os.getcwd()},
            "/images": {"tools.staticdir.on": True,
                        "tools.staticdir.dir": "images"},
            "/html": {"tools.staticdir.on": True,
                      "tools.staticdir.dir": "html"}
            }
    login_conf = {
            '/': {
                  'tools.sessions.on': True,
                  'tools.sessionFilter.on': True,
                  'tools.sessionFilter.filters': [],
                  "tools.staticdir.root": os.getcwd()
                  },
            "/images": {
                      "tools.staticdir.on": True,
                      "tools.staticdir.dir": "images"
                      },
            "/html": {
                    "tools.staticdir.on": True,
                    "tools.staticdir.dir": "html"
                    }
    }

    cherrypy.tree.mount(applicationContext.getComponent(componentId = "root"), '/', config=conf)
    cherrypy.tree.mount(applicationContext.getComponent(componentId = "loginForm"), '/login', config=login_conf)

    cherrypy.engine.start()
    cherrypy.engine.block()