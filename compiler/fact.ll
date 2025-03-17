; ModuleID = 'factorial'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

define i32 @factorial(i32 %n) {
  %ac = i32 0
  %counter = i32 1
  %end icmp eq %counter, %n

  br %end

  loop_body:
    alloca

  %s = sub i32 %a, 1
  %m = mul i32 %a, %s
  ret i32 %m
}

define i32 @main(i32 %0, ptr %1) {
  %result = call i32 @factorial(i32 5)
  ret i32 %result
}

