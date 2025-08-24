package lexer

import (
	"tarka/src/token"
)

type Lexer struct {
	input        string
	position     int
	readPosition int
	ch           byte
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

func (l *Lexer) NextToken() token.Token {
	var tok token.Token
	l.skipWhitespace()
	switch l.ch {
	case '=':
		tok = newToken(token.ASSIGN, "=")
	case ';':
		tok = newToken(token.SEMICOLON, ";")
	case ',':
		tok = newToken(token.COMMA, ",")
	case '.':
		tok = newToken(token.ILLEGAL, ".")
	case '+':
		tok = newToken(token.PLUS, "+")
	case '-':
		tok = newToken(token.MINUS, "-")
	case '*':
		tok = newToken(token.MULTIPLY, "*")
	case '/':
		tok = newToken(token.DIVIDE, "/")
	case 0:
		tok = newToken(token.EOF, "")
	default:
		if isLetter(l.ch) {
			tok.Literal = l.readIdentifier()
			tok.Type = token.LookupIdentifier(tok.Literal)
			return tok
		}
		if isDigit(l.ch) {
			tok.Literal = l.readNumber()
			tok.Type = l.getNumberType(tok.Literal)
			return tok
		}
	}
	l.readChar()
	return tok
}

func (l *Lexer) readIdentifier() string {
	position := l.position
	for isLetter(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]
}

func (l *Lexer) readNumber() string {
	position := l.position
	totalDecimals := 0
	for isDigit(l.ch) || l.ch == '.' {
		if l.ch == '.' && totalDecimals != 0 {
			return l.input[position:l.position]
		}
		if l.ch == '.' {
			totalDecimals++
		}
		l.readChar()
	}
	return l.input[position:l.position]
}

func (l *Lexer) getNumberType(num string) token.TokenType {
	for i := range len(num) {
		if num[i] == '.' {
			return token.FLOAT
		}
	}
	return token.INT
}

func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition++
}

func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\r' || l.ch == '\n' {
		l.readChar()
	}
}

func newToken(tokenType token.TokenType, literal string) token.Token {
	return token.Token{Type: tokenType, Literal: literal}
}

func isLetter(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}
