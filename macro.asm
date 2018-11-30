%macro a 2
%%abc:
	add eax,%1
	add ebx,%2
	mov eax,ebx
	mov edx,ecx
%endmacro
%macro c 2
%%abc:
	add eax,%1
	add ebx,%2
%endmacro
%macro d 2
%%pqr:
	add eax,%1
	add ebx,%2
%endmacro
section .text
	global main
	extern printf
main:
	a 10,20
	c 20,30
	d 40,2
	push eax
	call printf
	add esp,4
