package regex

// import

/////////////////////////
// TERMINALS
/////////////////////////

func is_start(char string) bool {
	return char == "^"
}

func is_end(char string) bool {
	return char == "$"
}

/////////////////////////
// OPERATORS
/////////////////////////

func is_star(char string) bool {
	return char == "*"
}

func is_plus(char string) bool {
	return char == "+"
}

func is_question(char string) bool {
	return char == "?"
}

func is_operator(char string) bool {
	return is_star(char) || is_plus(char) || is_question(char)
}

func is_dot(char string) bool {
	return char == "."
}

/////////////////////////
// DELIMETERS
/////////////////////////

func is_escape_sequence(term string) bool {
	return is_escape(string(term[0]))
}

func is_escape(char string) bool {
	return char == "\\"
}

func is_open_alternate(char string) bool {
	return char == "("
}

func is_close_alternate(char string) bool {
	return char == ")"
}

func is_open_set(char string) bool {
	return char == "["
}

func is_close_set(char string) bool {
	return char == "]"
}

func is_letter(s string) bool {
	for _, r := range s {
		if (r < 'a' || r > 'z') && (r < 'A' || r > 'Z') {
			return false
		}
	}
	return true
}

func is_digit(s string) bool {
	for _, r := range s {
		if r < '0' || r > '9' {
			return false
		}
	}
	return true
}

func is_literal(char string) bool {
	return is_digit(char) || is_letter(char)
}
