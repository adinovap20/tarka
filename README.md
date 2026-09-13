# Tarka

> Tarka is an experimental project under active design.

A minimal declarative UI DSL for building lightweight developer tools.

Tarka is a small language that lets developers describe simple user interfaces and compile them into HTML and CSS.

It is designed for developers like me who need quick, functional tools, without dealing with the complexity of modern frontend frameworks.

## Example

```tarka
Page hello {
  .title: "Hello World";

  Column {
    H1 {
      .text: "Welcome to Tarka";
    }
  }
}
```

## Philosophy

Tarka is intentionally minimal.

It focuses on:

- Developer tools
- Internal dashboards
- Small utilities
- Simple interfaces

It is not designed to replace full frontend frameworks or support every web development use case.

## Status

🚧 Early development

The project is currently in the design and prototyping phase.

## Goals

- Simple syntax
- Fast UI development
- Opinionated components
- Lightweight HTML/CSS generation
