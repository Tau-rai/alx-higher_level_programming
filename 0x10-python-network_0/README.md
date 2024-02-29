# README

This file explains various web concepts that are covered in this reposistory through project tasks.

## URL

A URL (Uniform Resource Locator) is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.

## HTTP

HTTP (Hypertext Transfer Protocol) is the protocol used for transferring data over the internet. It defines commands and services used for transmitting webpage data.

## Reading a URL

A URL generally consists of a protocol (like http), domain name, path, and query string. For example, in `http://example.com/path?query=value`, `http` is the protocol, `example.com` is the domain name, `/path` is the path, and `?query=value` is the query string.

## HTTP URL Scheme

The scheme for a HTTP URL begins with `http://` or `https://` for secure HTTP (HTTPS).

## Domain Name

A domain name is the part of a URL that uniquely identifies a website. For example, in `http://example.com`, `example.com` is the domain name.

## Sub-Domain

A sub-domain is a domain that is part of a larger domain. For example, in `http://sub.example.com`, `sub` is a sub-domain of `example.com`.

## Port Number in URL

A port number in a URL is defined after the domain name with a colon. For example, in `http://example.com:8080`, `8080` is the port number.

## Query String

A query string is a part of a URL that assigns values to specified parameters. It starts with a question mark (`?`). For example, in `http://example.com/path?query=value`, `?query=value` is the query string.

## HTTP Request

An HTTP request is made by a client to a server to fetch a resource. It includes a method (like GET or POST), headers, and sometimes a body.

## HTTP Response

An HTTP response is what is sent by a server to a client in response to an HTTP request. It includes a status code, headers, and the requested resource.

## HTTP Headers

HTTP headers let the client and the server pass additional information with an HTTP request or response.

## HTTP Message Body

The HTTP message body is the part of the request or response that carries the actual data.

## HTTP Request Method

An HTTP request method is a method that indicates the desired action to be performed on the specified resource. Examples include GET, POST, PUT, DELETE, etc.

## HTTP Response Status Code

An HTTP response status code is a status code that is returned by the server to let the client know the status of the requested resource. Examples include 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.

## HTTP Cookie

An HTTP cookie is a small piece of data stored on the user's computer by the web browser while browsing a website.

## Making a Request with cURL

cURL is a command-line tool used to make HTTP requests. Here's an example of a GET request: `curl http://example.com`.

## What Happens When You Type google.com in Your Browser

When you type `google.com` in your browser and hit enter, the browser performs several steps behind the scenes:

1. DNS Lookup: The browser looks up the IP address for the domain name via DNS.
2. HTTP Request: The browser sends an HTTP request to the server.
3. HTTP Response: The server handles the request and sends back an HTTP response.
4. Render: The browser renders the HTML content of the response.
