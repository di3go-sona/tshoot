# Tshoot

<p align="center">
    <em>A simple CLI command for troubleshooting errors with LLMs</em>
</p>

[![build](https://github.com/di3go-sona/tshoot/workflows/Build/badge.svg)](https://github.com/di3go-sona/tshoot/actions)
[![codecov](https://codecov.io/gh/di3go-sona/tshoot/graph/badge.svg?token=R4xWCp7AXq)](https://codecov.io/gh/di3go-sona/tshoot)
[![PyPI version](https://badge.fury.io/py/tshoot.svg)](https://badge.fury.io/py/tshoot)

---

**Documentation**: <a href="https://di3go-sona.github.io/tshoot/" target="_blank">https://di3go-sona.github.io/tshoot/</a>

**Source Code**: <a href="https://github.com/di3go-sona/tshoot" target="_blank">https://github.com/di3go-sona/tshoot</a>

---
## Introduction

The idea of tshoot is quite simple, by running the command `tshoot` you'll open a chat session with one of OpenAI's LLMs, you can dialogue with it and at the same time run commands by prefixing the line with `!`, the command will be executed on your local machine and the output will be displayed in the chat and added to the conversation history.

The main idea is to have a quick way to have your troubleshooting workflow overseen by an AI, potentially retrieving the information you need to solve your problem without any context switch, directly in your terminal.

The philosophy behind this project is to create a tool that should have minimal dependencies and should be easy to install and ready to use.

[![asciicast](https://asciinema.org/a/5UDk0XOruccA45eHF86usvEJy.svg)](https://asciinema.org/a/5UDk0XOruccA45eHF86usvEJy)

## Installation

You can install tshoot with pip:

```
pip install tshoot
```

## Development Setup


The project is packaged and shipped with [Hatch](https://hatch.pypa.io/latest/install/).
The following scripts are installed in your virtual environment:
-  `hatch run docs-build`
-  `hatch run docs-serve`
-  `hatch run lint`
-  `hatch run lint-check`
-  `hatch run test`
-  `hatch run test-cov-xml`


### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint
```


## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.


## Contributing

Every contribution that is in synch with the package philosofy is more than welcome, feel free to open an issue or submit a pull request.


## License

This project is licensed under the terms of the MIT license.
