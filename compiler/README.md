# DAT259 – Modern Compiler Construction Tools

## Compiler with LLVM

#### Start with the theory

1. Create a standard `Hello World` C file
2. Get a `LL` file with `clang -emit-llvm -S hello.c`
3. Connect to LLVM `export PATH="/opt/homebrew/Cellar/llvm/19.1.7_1/bin:$PATH"` (install LLVM with homebrew)
4. Get output `lli max.ll ; echo $?` from LL file

#### About LLVM

[LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html)

- Prefixes

  - `@` – global variables and functions
  - `%` – virtual register (only-once assignment)
  - `#` – attributes (metadata)
  - `!` – metadata

- Example of branching

  ```c
  ; ModuleID = 'max'
  target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
  target triple = "arm64-apple-macosx15.0.0"

  define i32 @max(i32 %a, i32 %b) {
    %c = icmp sgt i32 %a, %b

    br i1 %c, label %left_bigger, label %right_bigger

    left_bigger:
      ret i32 %a

    right_bigger:
      ret i32 %b
  }

  define i32 @main(i32 %0, ptr %1) {
    %result = call i32 @max(i32 13, i32 17)
    ret i32 %result
  }
  ```
