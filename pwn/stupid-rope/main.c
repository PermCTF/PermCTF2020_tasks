#include <stdio.h>

void lesson1(){
    printf("С помощью mov мы можем перемещать значения от источника к получателю.");
    __asm__("movl $0xf, %eax; ret;");
}

void lesson2(){
    printf("С помощью syscall мы обращаемся к ядру операционной системы для выполнения какой-либо операции.\n");
    __asm__("syscall; ret;");
}

void lesson3(){
    printf("NOP - это инструкция, которая предписывает процессору ничего не делать.\n");
    __asm__("nop; ret;");
}

void start_lesson(char *lesson){
    printf("[+] Вы выбрали урок %s\n", lesson);
    printf("Запуск уроков еще в разработке...\n");
}
int main(int argc, char **argv){
    char lesson[256];
    printf("[DEBUG] buf->%p\n", lesson);
    printf("Добро пожаловать в программу для изучения ассемблера\nВведите название урока: ");
    read(0, lesson, 1000); // очевидная уязвимость
    start_lesson(lesson);
    return 0;
}