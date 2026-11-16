# SOAP-API-PUBLIC-FETCH

# Module 5 Project Reflection

For this project, I recreated a SOAP-based Python application using a different public WSDL than the original example. I selected the German Bank-Code Service and modified the program to retrieve bank information instead of country information. The process involved researching the new service, updating the SOAP operations, adding input validation for the BLZ bank code, and converting the application to run as a Flask service with both GET and POST endpoints.

One thing that surprised me was how much of the SOAP interaction is handled automatically by the Zeep library after the WSDL is loaded. I also learned the importance of validating user input before sending requests to an external service. My code evolved from a simple command-line SOAP client into a small web service that could handle multiple requests through a browser, Postman, or curl.

A challenge I encountered was that the Thomas-Bayer SOAP endpoint appeared to be unavailable and returned connection errors when attempting to load the WSDL. Even though the service could not be reached, the application logic, validation, and Flask implementation were completed successfully. This project helped me better understand WSDL files, SOAP services, Flask routing, and API error handling. I would like to learn more about troubleshooting external web service availability and building more robust fault-tolerant API integrations.
