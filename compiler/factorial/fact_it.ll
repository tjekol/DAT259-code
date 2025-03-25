; ModuleID = 'factorial'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

define i32 @factorial(i32 %n) {
  %result = alloca i32
  %counter = alloca i32

  store i32 1, i32* %result 
  store i32 1, i32* %counter 

  br label %loop_body

  loop_cond:
    %counter_val = load i32, i32* %counter
    %c = icmp sle i32 %counter_val, %n
    br i1 %c, label %loop_body, label %loop_end

  loop_body:
    %curr_res = load i32, i32* %result
    %curr_count = load i32, i32* %counter
    
    %new_res = mul i32 %curr_res, %curr_count
    store i32 %new_res, i32* %result

    %upd_count = add i32 %curr_count, 1
    store i32 %upd_count, i32* %counter
    br label %loop_cond

  loop_end:
    %final_res = load i32, i32* %result
    ret i32 %final_res
}

define i32 @main(i32 %0, ptr %1) {
  %result = call i32 @factorial(i32 5)
  ret i32 %result
}

