#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void usage() {
  printf("Options:\n  1: List chats\n  2: Delete chat\n  3: Exit\n");
}

void list(char (*channels)[200]) {
  for(int i=0;i<5;i++) {
    printf("  %s\n",channels[i]);
  }

}

void delete(bool logged, char (*channels)[200], int value) {
  char c[5];
  char y[] = "yes";
  char *p;
  if(logged) {
    printf("Connection to backdoor...\n");
    sleep(2);
    printf("Deleting..\n");
    printf("Do you want add new instead? (yes or no)\n");
    fflush(stdout);
    fgets(c,5,stdin);
    if (strcmp(c,y)!=0) {
        printf("Input: ");
        fflush(stdout);
        fgets(channels[value],200,stdin);
        if ((p = strchr(channels[value], '\n')) != NULL)
            {*p = '\0';}
    }
    else{
        strcpy(channels[value],"deleted");
    }
  }
  else {
    printf("Access denied\n");
  }
}

void auth(bool *logged) {
  char captcha[8];
  const char user[] = "admin";
  const char pass[] = "h$bavb124";
  const int SIZE = 20;
  char username[SIZE];
  char password[SIZE];
  int a,b;
  printf("Username:\n");
  fflush(stdout);
  fgets(username, SIZE, stdin);
  printf("Password:\n");
  fflush(stdout);
  fgets(password, SIZE, stdin);
  a = rand() % 100;
  b = rand() % 100;
  printf("Captcha:%d + %d = ?\n",a,b);
  fflush(stdout);
  fgets(captcha,SIZE, stdin);
  if(strcmp(username,user) != 0 && strcmp(password,pass)!=0 && a+b==atoi(captcha)) {
    *logged = 1;
  }
  else {
    printf("Wrong\n");
  }
  return;
}

int main()
{
  bool logged = 0;
  char number[3];
  int number_int;
  char channels[5][200] ={
    "@durov",
    "@dc7342",
    "@dc7342_rules",
    "@mash",
    "@curiv",
  };

  char param[200];
  srand(time(NULL));
  printf("Hello to telegram chats banhammer\n");
  while (!feof(stdin)) {
    printf("Select option:\n");
    fflush(stdout);
    fgets(param,sizeof param,stdin);
    if (strlen(param)>133) {
      printf("Segmentation fault (core dumped)\n");
      exit(0);
    }
    switch(atoi(param)){
    case 1:
			list(channels);
			break;
		case 2:
      printf("Enter number:\n");
      fflush(stdout);
      fgets(number,sizeof number,stdin);
      printf("You selected:");
      printf(number);
      printf("\n");
      number_int = atoi(number);
			delete(logged, channels, number_int);
			break;
    case 3:
      exit(0);
    case 4:
      auth(&logged);
      break;
		default:
			usage();
    }
  }
  return 0;
}
