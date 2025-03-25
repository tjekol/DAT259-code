; ModuleID = 'factorial'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

; global variables uses @, local uses %
; sequence of bytes newline is \0A
@prompt = constant [12 x i8] c"Inputt er: \00"
@msg = constant [17 x i8] c"Fakultet er: %d\0A\00"
@format = constant [3 x i8] c"%d\00"

; printf, pointer and varg
declare i32 @printf (ptr, ...)

; scanf
declare i32 @scanf (ptr, ...)

define i32 @factorial(i32 %n) {
  entry:
    %c = icmp eq i32 %n, 0
    br i1 %c, label %base_case, label %recur

  base_case:
    ret i32 1

  recur:
    %s = sub i32 %n, 1
    %rr = call i32 @factorial(i32 %s)
    %res = mul i32 %n, %rr
    ret i32 %res
}

define i32 @main(i32 %0, ptr %1) {
  entry:
    call i32 (ptr, ...) @printf(ptr @prompt)
    %local_var = alloca i32
    call i32 (ptr, ...) @scanf(ptr @format, ptr %local_var)
    %input = load i32, ptr %local_var
    %result = call i32 @factorial(i32 %input)
    call i32 (ptr, ...) @printf(ptr @msg, i32 %input, i32 %result)
    ret i32 %result
}