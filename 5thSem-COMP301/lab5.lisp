;;Beginning of LISP journey
(format t "Hello, Sambeg!")

(terpri)
(terpri)

(format t "###########################~%    1. INTRODUCTION ~%###########################")
;;lisp is list processing so we mostly deal with lists

;;S-expression
;;Interpereted version
(format t "~%~%Add 69,4,20 = ")
(+ 69 4 20) 
;;Complied version
(write 
    (+ 69 4 20))

(terpri) ;; new line
(terpri) 

;;Value declaration to a variable ie Initialization using`(let ())`

(let 
    (
        (x 777) 
        (y 888))
    (princ "x= ")
    (princ x)
    (terpri)
    (princ "y= ")
    (princ y)
    (terpri)
    (princ "x + y = " )
    (princ 
        (+ x y)))

;;Note there is no order in execution of let arguments ie there is no order for initializing x and y
;;So,the following would result in an error
;;(let ((x 1)(y x))
;;    (terpri))

;;ERROR
;file:/home/sthasam/Programming/Labs/KU/COMP301-5thSem/lab5.lisp
;in:LET
;; (
;;     (X 1) 
;;     (Y X))
;(LET 
    ;; (
    ;;     (X 1) 
    ;;     (Y X))
;    (TERPRI))
;
;caughtWARNING:
;undefinedvariable:COMMON-LISP-USER::X
;
;compilationunitfinished
;Undefinedvariable:
;X
;caught1WARNINGcondition
;caught2STYLE-WARNINGconditions
;;Whileevaluatingtheformstartingatline28,column0
;;of#P"/home/sthasam/Programming/Labs/KU/COMP 301 - 5th Sem/lab5.lisp":x+y=1665


;;However for ordered execution let* note the asterisk (*) can be used.
;;So,following would not cause error
(terpri)
(terpri)

(let* 
    (
        (x 1)
        (y x))
    (princ "x= ")
    (princ x)
    (terpri)
    (princ "y= ")
    (princ y)
    (terpri)
    (princ "x + y = " )
    (princ 
        (+ x y)))

;;HELLO WORLD PROGRAM
;;A simple hello world program to write lines
(format t "~%~%Hello World Program~%___________________________~%")
(write-line "Hello World") ; prints hello world
(write-line "Hello, Sambeg Here on a journey to conquer LISP!")

(format t "~%#############################~%2. BASIC SYNTAX~%#############################~%")

;; LISP programs are made up of three basic building blocks −
;; -atom
;; -list
;; -string

;; An atom is a number or string of contiguous characters. It includes numbers and special characters.
;; Legal ones: 
;; -hello-from-tutorials-point
;; -name
;; -123008907
;; -*hello*
;; -Block#221
;; -abc123

;; A list is a sequence of atoms and/or other lists enclosed in parentheses.
;; -( i am a list)
;; -(a ( a b c) d e fgh)
;; -(father tom ( susan bill joe))
;; -(sun mon tue wed thur fri sat)
;; -( )

;; A string is a group of characters enclosed in double quotation marks.
;; -" I am a string"
;; -"a ba c d efg #$%^&!"
;; -"Please enter the following details :"
;; -"Hello from 'Tutorials Point'! "

(write-line "single quote used, it inhibits evaluation")
(write '(* 2 3))
(terpri)
(write-line "single quote not used, so expression evaluated")
(write (* 2 3))


(format t "~%#############################~%3. DATA TYPES~%#############################~%")

(format t "scalar data types: number types, characters, symbols, etc~%")
(format t "data structures: lists, vectors, bit-vectors, and strings~%")

(format t "~%Examples~%........................~%")
(format t "~%a) scalar data~%")

(setq s 10)
(setq a 34.567)
(setq m nil)
(setq b 123.78)
(setq e 11.0e+4)
(setq g 124/2)

(print s)
(print a)
(print m)
(print b)
(print e)
(print g)

(format t "~%~%types...")

(defvar s 10)
(defvar a 34.567)
(defvar m nil)
(defvar b 123.78)
(defvar e 11.0e+4)
(defvar g 124/2)
(defvar stha "sthasam")

(print (type-of s))
(print (type-of a))
(print (type-of m))
(print (type-of b))
(print (type-of e))
(print (type-of g))
(print (type-of stha))

(format t "~%~%#############################~%4. MACROS~%#############################~%")

(defmacro setTo10(num)
    (setq num 10)
    (format t "~%After setTo10, num= ")
    (princ num))

(setq num 25)
(format t "~%num= ")
(princ num)

(setTo10 num)


(format t "~%~%#############################~%5. VARIABLES~%#############################~%")

(format t "~%GLOBAL VARIABLES~%________________________~%~%")
(write-line "***`defvar` is used for declaring global variables***")


(defvar sambeg 69420)
(terpri)
(format t "Global sambeg = ")
(princ sambeg)

(terpri)
(defmacro printMessage(msg)
    (format t "~%inside macro sambeg = ")
    (princ sambeg)
    (format t "~%inside macro type of sambeg => ")
    (princ (type-of sambeg))
    (terpri))

(printMessage 42069)

(terpri)
(format t "Global sambeg after macro =")
(princ sambeg)

(terpri)
(terpri)
(setq sam 10)
(setq beg 20)
(format t "sam = ~2d; beg = ~2d ~%" sam beg)
(setq sam 100)
(setq beg 200)
(format t "sam = ~2d; beg = ~2d" sam beg)


(format t "~%~%LOCAL VARIABLES~%________________________~%~%")
(write-line "***`setq`, `let`, `prog` are used for declaring global variables***")

(format t "~%a) let~%")
(format t "SYNTAX: (let ((var1  val1) (var2  val2).. (varn  valn))<s-expressions>)~%")
(format t "~%Example.........~%")

(let ((x 'sam) (y 'beg)(z 'stha))
    (format t "x = ~a y = ~a z = ~a" x y z))

(format t "~%b) prog~%")
(format t "~%Example.........~%")
(prog (
    (x '(sam beg stha))
    (y '(1 2 3))
    (z '(four q 2)))
    (format t "x = ~a y = ~a z = ~a" x y z))

(terpri)
(terpri)

(format t "~%~%#############################~%6. CONSTANTS~%#############################~%")
(write-line "***`defconstant` is used for declaring constants***")

(defconstant PI 3.141592)
(defun area-circle(rad)
   (terpri)
   (format t "Radius:        ~5f" rad)
   (format t "~%Area:         ~10f" (* PI rad rad))
   (format t "~%Circumference:~10f" (* 2 PI rad)))

(area-circle 10)

(format t "~%~%#############################~%7. OPERATORS~%#############################~%")
(write-line "***The operations are categorized as: a)Arithmetic, b)Comparision, c) Logical, d)Bitwise***")
(format t "~%~%ARITHMETC~%________________________~%~%")

(setq A 69 B 420)

(defun add(a b)
    (setq result (+ a b))
    (format t "~2d + ~2d = ~2d" a b result))
(add A B)

(terpri)
(defun sub(a b)
    (setq result (- a b))
    (format t "~2d - ~2d = ~2d" a b result))
(sub B A)

(terpri)
(defun mul(a b)
    (setq result (* a b))
    (format t "~2d * ~2d = ~2d" a b result))
(mul 3 9)

(terpri)
(defun div(a b)
    (setq result (/ a b))
    (format t "~2d / ~2d = ~2d" a b result))
(div 27 9)

(terpri)
(defun modDiv(a b)
    (setq result (mod a b))
    (format t "~2d mod ~2d = ~2d" a b result))
(modDiv 27 7)

(terpri)
(defun modDivRem(a b)
    (setq result (rem a b))
    (format t "~2d rem ~2d = ~2d" a b result))
(modDivRem 100 11)

(terpri)
(defun increase(a b)
    (format t "a before incf = ~2d" a)
    (setq result (incf a b))
    (format t "; a after incf ~2d = ~2d" b result))
(increase 27 7)

(terpri)
(defun decrease(a b)
    (format t "a before decf = ~2d" a)
    (setq result (decf a b))
    (format t "; a after decf ~2d = ~2d" b result))
(decrease 100 11)

(format t "~%~%COMPARISION~%________________________~%~%")
(format t "~2d == ~2d? ~a" 11 11 (= 11 11))
(terpri)
(format t "~2d != ~2d? ~a" 11 11 (/= 11 11))
(terpri)
(format t "~2d > ~2d? ~a" 23423 17523457 (> 23423 17523457))
(terpri)
(format t "~2d < ~2d? ~a" 24234 423432 (< 24234 423432))
(terpri)
(format t "~2d >= ~2d? ~a" 31 2311 (>= 31 2311))
(terpri)
(format t "~2d <= ~2d? ~a" 12121 132131 (<= 12121 132131))
(terpri)
(format t "max among ~2d, ~2d? ~a" 12121 132131 (max 12121 132131))
(terpri)
(format t "min among ~2d, ~2d? ~a" 12121 132131 (min 12121 132131))

(format t "~%~%LOGICAL~%________________________~%~%")
(format t "~a and ~a? ~a" nil 11 (and nil 11))
(terpri)
(format t "~a or ~a? ~a" nil 121 (or 11 12))
(terpri)
(format t "not ~a? ~a" nil (not nil))
(terpri)
(format t "not ~a? ~a" 20 (not 20))
(terpri)

(format t "~%~%BITWISE~%________________________~%~%")
(setq a 60)
(setq b 13)

(format t "~% BITWISE AND of ~a and ~a is ~a" a b (logand a b))
(format t "~% BITWISE INCLUSIVE OR of ~a and ~a is ~a" a b (logior a b))
(format t "~% BITWISE EXCLUSIVE OR of ~a and ~a is ~a" a b (logxor a b))
(format t "~% ~a NOT ~a is ~a" a b (lognor a b))
(format t "~% ~a EQUIVALANCE ~a is ~a" a b (logeqv a b))

(terpri)

(setq a 10)
(setq b 0)
(setq c 30)
(setq d 40)

(format t "~% Result of bitwise and operation on 10, 0, 30, 40 is ~a" (logand a b c d))
(format t "~% Result of bitwise or operation on 10, 0, 30, 40 is ~a" (logior a b c d))
(format t "~% Result of bitwise xor operation on 10, 0, 30, 40 is ~a" (logxor a b c d))
(format t "~% Result of bitwise eqivalance operation on 10, 0, 30, 40 is ~a" (logeqv a b c d))

(format t "~%~%#############################~%7. CONDITIONALS/DECISION~%#############################~%")
(write-line "***The conditionals are categorized as: a)cond, b)if, c)when, d)case***")

(format t "~%~%COND~%________________________~%")

(setq a 10)
(format t "a=~a" a)
(cond ((> a 20)
    (format t "~% a is greater than 20"))
    (t (format t "~% value of a is ~d " a)))

(terpri)
(format t "~%~%IF~%________________________~%")

(setq a 10)
(format t "a=~a" a)
(if (> a 20)
    (format t "~% a is less than 20"))
(format t "~% value of a is ~d " a)

(terpri)
(format t "~%~%WHEN~%________________________~%")   

(setq a 100)
(format t "a=~a" a)
(when (> a 20)
    (format t "~% a is greater than 20"))
(format t "~% value of a is ~d " a)

(terpri)
(format t "~%~%CASE~%________________________~%")

(setq day 4)
(format t "day=~a" day)
(case day
    (1 
        (format t "~% Monday"))
    (2 
        (format t "~% Tuesday"))
    (3 
        (format t "~% Wednesday"))
    (4 
        (format t "~% Thursday"))
    (5 
        (format t "~% Friday"))
    (6 
        (format t "~% Saturday"))
    (7 
        (format t "~% Sunday")))

(terpri)


(format t "~%~%#############################~%8. LOOPS~%#############################~%")
(write-line "***The loops are categorized as: a)loop, b)loop for, c)do, d)dotimes, e)dolist***")

(format t "~%~%loop~%________________________~%")

(format t "~%Examples~%........................~%")
(setq a 10)
(loop 
    (setq a (+ a 1))
    (write a)
    (terpri)
    (when (> a 17) (return a))
)

(terpri)
(format t "~%~%loop for~%________________________~%")

(format t "~%Examples~%........................~%")

(format t "~%~%Example 1~%")
(loop for x in '(tom dick harry)
    do (format t " ~s" x)
)

(format t "~%~%Example 2~%")
(loop for a from 10 to 20
    do (print a)
)

(terpri)
(format t "~%~%do~%________________________~%")

(format t "~%Examples~%........................~%")
(do ((x 0 (+ 2 x))
    (y 20 ( - y 2)))
    ((= x y)(- x y))
    (format t "~% x = ~d  y = ~d" x y)
)

(terpri)
(format t "~%~%dotimes~%________________________~%")

(format t "~%Examples~%........................~%")
(dotimes (n 11)
    (print n) (prin1 (* n n))
)

(terpri)
(format t "~%~%dolist~%________________________~%")

(format t "~%Examples~%........................~%")
(dolist (n '(1 2 3 4 5 6 7 8 9))
    (format t "~% Number: ~d Square: ~d" n (* n n))
)

(terpri)
(write-line "***The ways to exit loop are : a)block return-from ***")

(format t "~%Examples~%........................~%")
(defun demo-function (flag)
    (block outer-block
        (print 'entered-outer-block)
        ;; (format t "~%outer flag=~a" flag)
        (print 
            (if (not flag)
                ;; when true
                (return-from outer-block 3)
                ;;  when false
                (block inner-block
                    (print 'entered-inner-block)
                    ;; (format t "~%inner flag=~a" flag)
                    (if flag
                        ;; when true
                        (return-from inner-block 5)
                        ;; when false
                        (print "this will not be printed")
                    )
                )
            )
        t)
        (print 'left-inner-block)
    )
    (print 'left-outer-block)
)
(demo-function t)
(terpri)
(demo-function nil)


(format t "~%~%#############################~%9. FUNCTIONS~%#############################~%")
(write-line "***`defun` is usd to define functions***")

(format t "~%Examples~%........................~%")

(defun averagenum (n1 n2 n3 n4)
    (/ ( + n1 n2 n3 n4) 4)
)
(format t "average of 10 20 30 40 = ~a" (averagenum 10 20 30 40))

(format t "~%~%#############################~%10. PREDICATES~%#############################~%")
(write-line "***Predicates are functions that test their arguments for some specific conditions and returns nil if the condition is false, or some non-nil value is the condition is true***")

(format t "~%Examples~%........................~%")
(format t "~%Example 1~%")
(format t "Is atom ~a? ~a" 'abcd' (atom 'abcd))
(terpri)
(format t "Is equal ~a & ~a? ~a" 'a' 'b' (equal 'a 'b))
(terpri)
(format t "Is evenp ~a? ~a" 10 (evenp 10))
(terpri)
(format t "Is evenp ~a? ~a" 7 (evenp 7 ))
(terpri)
(format t "Is oddp ~a? ~a" 7 (oddp 7 ))
(terpri)
(format t "Is zerop ~a? ~a" 0.0000000001 (zerop 0.0000000001))
(terpri)
(format t "Is eq ~a & ~a? ~a" 3 3.0 (eq 3 3.0 ))
(terpri)
(format t "Is equal ~a & ~a? ~a" 3 3.0 (equal 3 3.0 ))
(terpri)
(format t "Is null ~a? ~a" nil (null nil ))

(format t "~%~%Example 2~%")
(defun factorial (num)
    (cond 
        ((zerop num) 1)
        (t 
            ( * num (factorial (- num 1)))
        )
    )
)
(setq n 6)
(format t "~% Factorial ~d is: ~d" n (factorial n))
(format t "~% Factorial ~d is: ~d" 0 (factorial 0))

(format t "~%~%#############################~%11. NUMBERS~%#############################~%")
(format t "~%Types: Integers, Ratios, Floating-point numbers, Complex numbers~%")

(format t "~%Types~%........................~%")
(format t "~a : ~a" (/ 1 2) (type-of (/ 1 2)))
(terpri)
(format t "~a : ~a"  ( + (/ 1 2) (/ 3 4)) (type-of (+ (/ 1 2) (/ 3 4))))
(terpri)
(format t "~a : ~a" ( + #c( 1 2) #c( 3 -4))(type-of (+ #c( 1 2) #c( 3 -4))))
(terpri)


(format t "~%Functions~%........................~%")
(format t "~%Example 1~%")

(write (/ 45 78))
(terpri)
(write (floor 45 78))
(terpri)
(write (/ 3456 75))
(terpri)
(write (floor 3456 75))
(terpri)
(write (ceiling 3456 75))
(terpri)
(write (truncate 3456 75))
(terpri)
(write (round 3456 75))
(terpri)
(write (ffloor 3456 75))
(terpri)
(write (fceiling 3456 75))
(terpri)
(write (ftruncate 3456 75))
(terpri)
(write (fround 3456 75))
(terpri)
(write (mod 3456 75))
(terpri)
(setq c (complex 6 7))
(write c)
(terpri)
(write (complex 5 -9))
(terpri)
(write (realpart c))
(terpri)
(write (imagpart c))


(format t "~%~%#############################~%12. CHARS~%#############################~%")
(format t "~%\# denotes the characters itsel")

(format t "~%Character objects~%........................~%")

(write 'a)
(terpri)
(write #\a)
(terpri)
(write-char #\a)
;; (terpri)
;; (write-char 'a)


(format t "~%Functions~%........................~%")
(format t "~%Example 1~%")

; case-sensitive comparison
(write (char= #\a #\b))
(terpri)
(write (char= #\a #\a))
(terpri)
(write (char= #\a #\A))
(terpri)

;case-insensitive comparision
(write (char-equal #\a #\A))
(terpri)
(write (char-equal #\a #\b))
(terpri)
(write (char-lessp #\a #\b #\c))
(terpri)
(write (char-greaterp #\a #\b #\c))


(format t "~%~%#############################~%13. ARRAY~%#############################~%")
(format t "~%`make-array` func creates an array")

(format t "~%Examples~%........................~%")
(format t "~%Example 1~%")

(format t "before assigning values creating an array")
(terpri)
(write (setf my-array (make-array '(10))))
(terpri)
(setf (aref my-array 0) 25)
(setf (aref my-array 1) 23)
(setf (aref my-array 2) 45)
(setf (aref my-array 3) 10)
(setf (aref my-array 4) 20)
(setf (aref my-array 5) 17)
(setf (aref my-array 6) 25)
(setf (aref my-array 7) 19)
(setf (aref my-array 8) 67)
(setf (aref my-array 9) 30)
(terpri)
(format t "after assigning values to array")
(terpri)
(write my-array)
(terpri)

(format t "~%Example 2: multi dimentional array~%")
(setf x (make-array '(3 3) 
   :initial-contents '((0 1 2 ) (3 4 5) (6 7 8)))
)
(write x)
(terpri)

(format t "~%Example 3: multi dimentional array with arguments and description~%")
(setq myarray (make-array '(3 2 3) 
   :initial-contents 
   '(((a b c) (1 2 3)) 
      ((d e f) (4 5 6)) 
      ((g h i) (7 8 9)) 
   ))
) 
(setq array2 (make-array 4 :displaced-to myarray :displaced-index-offset 2)) 
(write myarray)
(terpri)
(write array2)

(terpri)

(format t "~%Example 4: Arrays using different properties~%")

;a one dimensional array with 5 elements, 
;initail value 5
(write (make-array 5 :initial-element 5))
(terpri)

;two dimensional array, with initial element a
(write (make-array '(2 3) :initial-element 'a))
(terpri)

;an array of capacity 14, but fill pointer 5, is 5
(write(length (make-array 14 :fill-pointer 5)))
(terpri)

;however its length is 14
(write (array-dimensions (make-array 14 :fill-pointer 5)))
(terpri)

; a bit array with all initial elements set to 1
(write(make-array 10 :element-type 'bit :initial-element 1))
(terpri)

; a character array with all initial elements set to a
; is a string actually
(write(make-array 10 :element-type 'character :initial-element #\a)) 
(terpri)

; a two dimensional array with initial values a
(setq myarray (make-array '(2 2) :initial-element 'a :adjustable t))
(write myarray)
(terpri)

;readjusting the array
(adjust-array myarray '(1 3) :initial-element 'b) 
(write myarray)


(format t "~%~%#############################~%14. STRINGS~%#############################~%")

;; 
(write-line "Hello World")
(write-line "Welcome to Tutorials Point")

;escaping the double quote character
(write-line "Welcome to \"Tutorials Point\"")

(write-line "Hello World")
(write-line "Welcome to Tutorials Point")

;escaping the double quote character
(write-line "Welcome to \"Tutorials Point\"")
;; 

; case-sensitive comparison
(write (string= "this is test" "This is test"))
(terpri)
(write (string> "this is test" "This is test"))
(terpri)
(write (string< "this is test" "This is test"))
(terpri)

;case-insensitive comparision
(write (string-equal "this is test" "This is test"))
(terpri)
(write (string-greaterp "this is test" "This is test"))
(terpri)
(write (string-lessp "this is test" "This is test"))
(terpri)

;checking non-equal
(write (string/= "this is test" "this is Test"))
(terpri)
(write (string-not-equal "this is test" "This is test"))
(terpri)
(write (string/= "lisp" "lisping"))
(terpri)
(write (string/= "decent" "decency"))
;; 

(write-line "Case Controlling Functions")
(write-line (string-upcase "a big hello from tutorials point"))
(write-line (string-capitalize "a big hello from tutorials point"))

;; 
(write-line "Trimming Strings Functions")

(write-line (string-trim " " "   a big hello from tutorials point   "))
(write-line (string-left-trim " " "   a big hello from tutorials point   "))
(write-line (string-right-trim " " "   a big hello from tutorials point   "))
(write-line (string-trim " a" "   a big hello from tutorials point   "))

;; 


(format t "~%~%#############################~%15. SEQUESNCES~%#############################~%")

(write (make-sequence '(vector float) 
   10 
   :initial-element 1.0))

(format t "~%~%#############################~%16. LISTS~%#############################~%")

(write (list 1 2))
(terpri)
(write (list 'a 'b))
(terpri)
(write (list 1 nil))
(terpri)
(write (list 1 2 3))
(terpri)
(write (list 'a 'b 'c))
(terpri)
(write (list 3 4 'a (car '(b . c)) (* 4 -2)))
(terpri)
(write (list (list 'a 'b) (list 'c 'd 'e)))

(format t "~%~%Manipulations~%")

(write (car '(a b c d e f)))
(terpri)
(write (cdr '(a b c d e f)))
(terpri)
(write (cons 'a '(b c)))
(terpri)
(write (list 'a '(b c) '(e f)))
(terpri)
(write (append '(b c) '(e f) '(p q) '() '(g)))
(terpri)
(write (last '(a b c d (e f))))
(terpri)
(write (reverse '(a b c d (e f))))

(format t "~%~%#############################~%17. SYMBOLS~%#############################~%")
(write-line "Example 1")
(write (setf (get 'books'title) '(Gone with the Wind)))
(terpri)
(write (setf (get 'books 'author) '(Margaret Michel)))
(terpri)
(write (setf (get 'books 'publisher) '(Warner Books)))


(write-line "Example 2")
(setf (get 'annie 'age) 43)
(setf (get 'annie 'job) 'accountant)
(setf (get 'annie 'sex) 'female)
(setf (get 'annie 'children) 3)

(terpri)
(write (symbol-plist 'annie))
(remprop 'annie 'age)
(terpri)
(write (symbol-plist 'annie))

(format t "~%~%#############################~%18. VECTORS~%#############################~%")

(write-line "Example 1")
(setf v1 (vector 1 2 3 4 5))
(setf v2 #(a b c d e))
(setf v3 (vector 'p 'q 'r 's 't))

(write v1)
(terpri)
(write v2)
(terpri)
(write v3)



(write-line "Example 3")
(setq a (make-array 5 :fill-pointer 0))
(write a)

(vector-push 'a a)
(vector-push 'b a)
(vector-push 'c a)

(terpri)
(write a)
(terpri)

(vector-push 'd a)
(vector-push 'e a)

;this will not be entered as the vector limit is 5
(vector-push 'f a)

(write a)
(terpri)

(vector-pop a)
(vector-pop a)
(vector-pop a)

(write a)

;; (format t "~%~%#############################~%19. SET~%#############################~%")
;; (format t "~%~%#############################~%20. TREE~%#############################~%")
;; (format t "~%~%#############################~%21. HASH TABLE~%#############################~%")
;; (format t "~%~%#############################~%21. I/O~%#############################~%")
;; (format t "~%~%#############################~%21. FILE I/O~%#############################~%")


(format t "~%~%#############################~%21. STRUCTURES~%#############################~%")
(write-line "Example 1")
(terpri)
(defstruct book 
   title 
   author 
   subject 
   book-id 
)

( setq book1 (make-book :title "C Programming"
   :author "Nuha Ali" 
   :subject "C-Programming Tutorial"
   :book-id "478")
)

( setq book2 (make-book :title "Telecom Billing"
   :author "Zara Ali" 
   :subject "C-Programming Tutorial"
   :book-id "501")
) 

(write book1)
(terpri)
(write book2)
(setq book3( copy-book book1))
(setf (book-book-id book3) 100) 
(terpri)
(write book3)
;; (format t "~%~%#############################~%21. PACKAGES~%#############################~%")


(format t "~%~%#############################~%21. ERROR HANDLING~%#############################~%")

(define-condition on-division-by-zero (error)
    ((message :initarg :message :reader message))
)
    
(defun handle-infinity ()
    (restart-case
        (let ((result 0))
            (setf result (division-function 10 0))
            (format t "Value: ~a~%" result)
        )
        (just-continue () nil)
    )
) 
    
(defun division-function (value1 value2)
    (restart-case
        (if (/= value2 0)
            (/ value1 value2)
            (error 'on-division-by-zero :message "denominator is zero")
        )

        (return-zero () 0)
        (return-value (r) r)
        (recalc-using (d) (division-function value1 d))
    )
)

(defun high-level-code ()
    (handler-bind
        (
            (on-division-by-zero
            #'(lambda (c)
                (format t "error signaled: ~a~%" (message c))
                (invoke-restart 'return-zero)
            )
            )
            (handle-infinity)
        )
    )
)

(handler-bind
    (
        (on-division-by-zero
            #'(lambda (c)
            (format t "error signaled: ~a~%" (message c))
            (invoke-restart 'return-value 1)
            )
        )
    )
    (handle-infinity)
)

(handler-bind
    (
        (on-division-by-zero
            #'(lambda (c)
                (format t "error signaled: ~a~%" (message c))
                (invoke-restart 'recalc-using 2)
            )
        )
    )
    (handle-infinity)
)

(han dler-bind
    ( 
        (on-division-by-zero
            #'(lambda (c)
                (format t "error signaled: ~a~%" (message c))
                (invoke-restart 'just-continue)
            )
        )
    ) 
    (handle-infinity)
)

(format t "Done.")
