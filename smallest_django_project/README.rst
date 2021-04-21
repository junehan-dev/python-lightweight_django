Hello Django
============

Basic
-----

Summary
^^^^^^^
   - Django Referred to as *model-template-view MTV framework*
   - What does *view portion* do?
      view portion inspects the incomming HTTP req and quries, or contructs, the necessray data to send to the *Presentation layer.*

1. hello.py with basic view
^^^^^^^^^^^^^^^^^^^^^^^^^^^
   - implement index function
   - implement url for above
   - implement settings
   - implement main routine statement
      - execute from command line function call at ``django.core.management``
Conclusion
^^^^^^^^^^
   - Django also provides additional utilities for common tasks involved in handlling HTTP requests, such as rendering HTML, parsing form data, and persisting session state.
      - It is important to understand how these features can be used in your application in a lightweight manner.

2. WSGI Application
-------------------

Summary
^^^^^^^
   - Above were simple server based on socket server in standard library. (but not appropriate for production deployment security)
   - WSGI is specification for how web servers communicate with application frameworks such as django (defined in PEP333 and improved 3333)
   - WSGI app, *Apache via mod_wsgi, Gunicorn, uWSGI, CHerryPy, Tornado, Chaussette.*

Conclusion
^^^^^^^^^^
   - The Process ID for the arbiter and the worker will also be different.

3. Additional configuration
---------------------------

Summary
^^^^^^^
   - Gunicorn is production ready web server.
      - But application itself is not yet,
         - as DEBUG should never be enabled in production.
         - as SECRET_KEY is also stored temporary with generated random.

Conclusion
^^^^^^^^^^
   - Twelve Factor App is Methodology for HTTP service applications.
      - This methodology recommends **separating configuration and code as well as storing configurations in environment variables.**
      - This make Easy to chang on the deployment and configuration OS-agnostic.


4. Resuable Template
--------------------

Summary
^^^^^^^
   - command ``django-admin startproject config .`` actually generates default templates, but we can customize our own.
   - ``django-admin startproject myproject --template=directory_name``
