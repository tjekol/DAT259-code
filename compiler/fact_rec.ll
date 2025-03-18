; ModuleID = 'factorial'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

define i32 @factorial(i32 %n) {
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
  %result = call i32 @factorial(i32 5)
  ret i32 %result
}