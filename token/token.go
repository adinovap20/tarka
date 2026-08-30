package token

type TokenType string

type Token struct {
	Type TokenType
	Lit  string
}

const (
	EX_UNKNOWN = "EX_UNKNOWN"
	EX_NEWLINE = "EX_NEWLINE"
	EX_EOF     = "EX_EOF"

	KW_EXIT = "KW_EXIT"

	LIT_IDENT = "LIT_IDENT"
	LIT_INT   = "LIT_INT"
)

var keywords = map[string]TokenType{
	"Exit": KW_EXIT,
}

func LookupIdent(ident string) TokenType {
	if tok, ok := keywords[ident]; ok {
		return tok
	}
	return LIT_IDENT
}
