package repl

import (
	"bufio"
	"fmt"
	"io"

	"github.com/adinovap20/tarka/lexer"
	"github.com/adinovap20/tarka/token"
)

const PROMPT = ">> "

func Start(in io.Reader, out io.Writer) {
	scanner := bufio.NewScanner(in)
	err := scanner.Err()
	if err != nil {
		fmt.Println("Scanner could not be created")
		return
	}

	for {
		fmt.Printf(PROMPT)
		scanned := scanner.Scan()
		if !scanned {
			return
		}

		line := scanner.Text()

		l := lexer.New(line)

		for tok := l.NextToken(); tok.Type != token.EX_EOF; tok = l.NextToken() {
			fmt.Printf("%+v\n", tok)
		}
	}
}
