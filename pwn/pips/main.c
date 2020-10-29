#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void usage() {
  printf("Options:\n  1: List cities\n  2: Rename city\n  3: Exit\n");
}

void list(char (*cities)[200]) {
  for(int i=0;i<5;i++) {
    printf("  %s\n",cities[i]);
  }

}

void rename_city(bool logged, char (*cities)[200], int value) {
  char *p;
  if(logged) {
    printf("Connection to government...\n");
    sleep(2);
    printf("New name: ");
    fflush(stdout);
    fgets(cities[value],200,stdin);
    if ((p = strchr(cities[value], '\n')) != NULL)
            {*p = '\0';}
  }
  else {
    printf("Access denied\n");
  }
}

void auth(bool *logged) {
  char captcha[8];
  const char user[] = "admin";
  const char pass[] = "h$bavb124";
  const int SIZE = 32;
  int count = 5;
  char username[SIZE];
  char password[SIZE];
  int a,b;
  while (count != 0) {
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
    read(0,captcha,48);
    printf("You entered:");
    printf(captcha);
    if(strcmp(username,user) != 0 && strcmp(password,pass)!=0 && a+b==atoi(captcha)) {
      *logged = 1;
      return;
    }
    else {
      printf("Wrong\n");
      count -=1;
      printf("%d attempts left\n",count);
    }
  }
  exit(-1);
}

int main()
{
  bool logged = 0;
  char number[4];
  int number_int;
  char cities[5][200] ={
    "Alma-Ata",
    "Nur-Sultan",
    "Shimkent",
    "Actobe",
    "Karaganda",
  };

  char param[200];
  srand(time(NULL));
  printf("Hello to city renamer bot\n");
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
			list(cities);
			break;
		case 2:
      printf("Enter number:\n");
      fflush(stdout);
      fgets(number,sizeof number,stdin);
      number_int = atoi(number);
			rename_city(logged, cities, number_int);
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
