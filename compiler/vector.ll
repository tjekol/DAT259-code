; ModuleID = 'vector'
source_filename = 'vector'
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx15.0.0"

@msg = constant [21 x i8] c"Last element is: %d\0A\00"
@stat_msg = constant [24 x i8] c"Size: %d\0A\00"
%Vector = type {
  ptr, 
  i64, 1 = size
  i64, 2 = capacity
}

; taken from libc
declare i32 @printf (ptr, ...)
declare ptr @malloc (i64)
declare void @free (ptr)
declare ptr @memcpy (ptr, ptr, i64)

define i32 @main(i32 %argc, ptr %argv) {
  %mem = call ptr (i64) @malloc(i64 4)
  
  %idx1 = getElementptr i8 ptr %mem, i64 0
  %idx2 = getElementptr i8 ptr %mem, i64 1
  %idx3 = getElementptr i8, ptr %mem, i64 2
  %idx4 = getElementptr i8, ptr %mem, i64 3

  store i8
}