package lexer

import (
	"github.com/adinovap20/tarka/token"
)

type Lexer struct {
	code    string
	pos     int
	readPos int
	ch      byte
}

func New(code string) *Lexer {
	l := &Lexer{code: code}
	l.readChar()
	return l
}

func (l *Lexer) NextToken() token.Token {
	var tok token.Token

	l.skipWhitespace()

	switch l.ch {
	case '\n':
		tok.Lit = "\n"
		tok.Type = token.EX_NEWLINE
	case 0:
		tok.Lit = ""
		tok.Type = token.EX_EOF
	default:
		if isLetter(l.ch) {
			tok.Lit = l.readIdentifier()
			tok.Type = token.LookupIdent(tok.Lit)
			return tok
		} else if isDigit(l.ch) {
			tok.Lit = l.readNumber()
			tok.Type = token.LIT_INT
			return tok
		} else {
			tok.Type = token.EX_UNKNOWN
			tok.Lit = ""
		}
	}

	l.readChar()
	return tok
}

func (l *Lexer) readChar() {
	if l.readPos >= len(l.code) {
		l.ch = 0
	} else {
		l.ch = l.code[l.readPos]
	}
	l.pos = l.readPos
	l.readPos++
}

func (l *Lexer) skipWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\r' {
		l.readChar()
	}
}

func (l *Lexer) readIdentifier() string {
	position := l.pos
	for isAlnum(l.ch) {
		l.readChar()
	}
	return l.code[position:l.pos]
}

func (l *Lexer) readNumber() string {
	position := l.pos
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.code[position:l.pos]
}

func isLetter(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

func isAlnum(ch byte) bool {
	return isLetter(ch) || isDigit(ch)
}
