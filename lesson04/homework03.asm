%include 'library.asm'

section .text
    global _start

_start:
    mov ecx,len
    mov edx,0	

loop:
    movsx eax,byte[ar+edx]
    call print_number1    
    mov eax,','
    call printChar
    inc edx
    dec ecx
    jnz loop
    
    mov eax,0x0A	
    call printChar

    ;обрабатываем
    mov ecx,len
    mov edx,0 
loop1:
   movsx eax,byte[ar+edx]
   call getValue
   mov byte[result+edx],al 
   call print_number1
   mov eax,','
   call printChar
   inc edx
   dec ecx
   jnz loop1 	

   mov eax,0x0A
   call printChar

   call exit
 	
getValue:
    pushad
    movsx ecx,byte[max]	
    cmp eax,ecx    
    jg maxVal	
    movsx ecx,byte[prev]
    cmp eax,ecx
    jg prevVal
    mov byte[tmp], cl
    mov byte[prev],al
    popad
    movsx eax,byte[tmp]   
    ret
prevVal:
    mov byte [prev],al
    popad
    movsx eax,byte[max]
    ret
maxVal:
    mov byte [max],al
    mov byte [prev],al
    popad
    mov eax,-1
    ret

section .data

ar      db	17, 21, 13, 17, 14, 12      
len     equ     $ - ar

segment .bss
    result: resb len
    prev:  resb 1
    max:   resb 1
    tmp:   resb 1
