#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void exec (char *command) {
  FILE *fp;
  char captcha[8];
  int a,b;
  char output[1000];
  char com[100];
  char userinput[100];
  a = rand() % 100;
  b = rand() % 100;
  printf("Captcha: %d + %d = ?\n",a,b);
  fflush(stdout);
  fgets(captcha,8,stdin);
  strcpy(com,command);
  if (a+b==atoi(captcha)) {
    if (!strcmp(com,"cat ")) {
      printf("Enter file to read from current directory: ");
      fflush(stdout);
      fgets(userinput,100,stdin);
      if(strstr(userinput,"flag") || strstr(userinput,"../")) {
        printf("Hacker detected, exit");
        exit(1);
      }
      strcat(com,userinput);
     }
    fp = popen(com,"r");
    while (fgets(output, sizeof(output), fp) != NULL) {
      printf("%s", output);
    }
    fflush(stdout);
    fclose(fp);
  }
}
int main(){
  srand ( time(NULL) );
  printf("This program execute random system command\n");
  char commands[5][120] = {
    "uname -a",
    "whoami",
    "pwd",
    "ls",
    "cat ",
  };
  while (!feof(stdin)) {
    char *command = commands[rand() % 5];
#ifdef DEBUG
    exec("cat ");
#else
    exec(command);
#endif

  }

}
