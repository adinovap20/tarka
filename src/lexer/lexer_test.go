package lexer

import (
	"fmt"
	"tarka/src/token"
	"testing"
)

func TestNextToken(t *testing.T) {
	cur := 0
	{
		// Set 1 : Basic Expressions
		cur = 1
		input := "x = 1; __ab_c, abc = 2, 212;"
		tests := []struct {
			expectedType    token.TokenType
			expectedLiteral string
		}{
			{token.IDENT, "x"},
			{token.ASSIGN, "="},
			{token.INT, "1"},
			{token.SEMICOLON, ";"},
			{token.IDENT, "__ab_c"},
			{token.COMMA, ","},
			{token.IDENT, "abc"},
			{token.ASSIGN, "="},
			{token.INT, "2"},
			{token.COMMA, ","},
			{token.INT, "212"},
			{token.SEMICOLON, ";"},
			{token.EOF, ""},
		}
		l := New(input)
		for i, tt := range tests {
			tok := l.NextToken()
			if tok.Type != tt.expectedType {
				t.Fatalf("set[%d],tests[%d] - token type wrong. Expected=%q; Got=%q", cur, i, tt.expectedType, tok.Type)
			}
			if tok.Literal != tt.expectedLiteral {
				t.Fatalf("set[%d],tests[%d] - token literal wrong. Expected=%q; Got=%q", cur, i, tt.expectedLiteral, tok.Literal)
			}
			fmt.Printf("set[%d],tests[%d] - Success\n", cur, i)
		}
	}
	{
		// Set 2 : Printing support
		cur = 2
		input := "x = 1; vad x;"
		tests := []struct {
			expectedType    token.TokenType
			expectedLiteral string
		}{
			{token.IDENT, "x"},
			{token.ASSIGN, "="},
			{token.INT, "1"},
			{token.SEMICOLON, ";"},
			{token.VAD, "vad"},
			{token.IDENT, "x"},
			{token.SEMICOLON, ";"},
		}
		l := New(input)
		for i, tt := range tests {
			tok := l.NextToken()
			if tok.Type != tt.expectedType {
				t.Fatalf("set[%d],tests[%d] - token type wrong. Expected=%q; Got=%q", cur, i, tt.expectedType, tok.Type)
			}
			if tok.Literal != tt.expectedLiteral {
				t.Fatalf("set[%d],tests[%d] - token literal wrong. Expected=%q; Got=%q", cur, i, tt.expectedLiteral, tok.Literal)
			}
			fmt.Printf("set[%d],tests[%d] - Success\n", cur, i)
		}
	}
}
