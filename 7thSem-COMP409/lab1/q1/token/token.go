package token

import (
	"encoding/csv"
	"io"
	"log"
	"os"
)

type TokenType string

// constant declaration for various tokens
const (
	ILLEGAL = "ILLEGAL"
	EOF     = "EOF"

	// Identifiers + literals
	IDENT = "IDENT" // add, foobar, x, y, ...
	INT   = "INT"   // 1343456

	// Operators
	ASSIGN   = "="
	PLUS     = "+"
	MINUS    = "-"
	BANG     = "!"
	ASTERISK = "*"
	SLASH    = "/"

	LT = "<"
	GT = ">"

	EQ     = "=="
	NOT_EQ = "!="

	// Delimiters
	COMMA     = ","
	SEMICOLON = ";"

	LPAREN = "("
	RPAREN = ")"
	LBRACE = "{"
	RBRACE = "}"

	// Keywords
	KEYWORD = "KEYWORD"
)

// custom token data type
type Token struct {
	Type    TokenType
	Literal string
}

// reading keywords
var keywords = ReadKeywordsFromCSV()

// checking identity is keyword and returning keyword's particular token else identity
//
// Eg, int is keyword so returns KEYWORD
// Eg, a is not keyword so returns IDENT
func LookupIdent(ident string) TokenType {
	if tok, ok := keywords[ident]; ok {
		return tok
	}
	return IDENT
}

// function for reading keywords from csv
func ReadKeywordsFromCSV() map[string]TokenType {
	f, err := os.Open("keywords.csv")

	if err != nil {

		log.Fatal(err)
	}

	r := csv.NewReader(f)
	extractedKeywords := make(map[string]TokenType)
	for {
		record, err := r.Read()

		if err == io.EOF {
			break
		}

		if err != nil {
			log.Fatal(err)
		}

		for value := range record {
			extractedKeywords[record[value]] = KEYWORD
		}
	}

	return extractedKeywords
}
