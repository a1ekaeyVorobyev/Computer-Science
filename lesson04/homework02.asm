%include 'library.asm'

section .text
    global _start

_start:

    mov ebp,  ar                ; записываем указатель на массив
    dec ebp
    mov  ecx, len               ;записываем размер массива
    mov  eax,[cf]		;записывем текущий этаж
loop:
    cmp byte[ebp+ecx],'u'       ;смотрим u или d значение
    je Up			
    dec eax
pr:
    dec ecx
    jnz loop
    call print_number
    call exit
Up:
    inc eax	
    jmp pr

section .data

ar      db      'u', 'd', 'd', 'u', 'u', 'd', 'd', 'u','u'
len     equ     $ - ar
cf	dd	4
