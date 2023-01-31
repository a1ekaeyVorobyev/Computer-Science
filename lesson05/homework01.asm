%include 'library.asm'

section .text
    global _start

_start:

    mov ebp,  ar     		; записываем указатель на массив 
    dec ebp
    mov  ecx, len  		;записываем размер массива	
loop:
    test byte[ebp+ecx],1 	;смотрим 0 или 1 значение
    jnz One
    cmp ebx,edx 
    call MaxValue
    xor edx,edx 
pr:
    dec ecx
    jnz loop
    call MaxValue
    mov eax,ebx
    call print_number		
    call exit
One:
    inc edx
    jmp pr

MaxValue:
    cmp ebx,edx
    jl Val
    ret 
Val: 
    mov ebx,edx
    ret

section	.data

ar 	db 	1,1,1,1,1,0,0,1,0,1,1,1,0,1
len	equ	$ - ar			;length of our dear string










