// build: 1)  gcc main.c -z execstack -no-pie -fno-stack-protector -static -o main
//        2) echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <unistd.h>
#include <time.h>

int running = 1;
struct account
{
    char nickname[24];
    char password[32];
};

void cat_flag(){
    char flag[30];
    FILE* flag_p = fopen("flag", "r");
    fgets(flag, 30, flag_p);
    printf("%s\n", flag);
    fflush(stdout);
    exit(0);
}

void clear_screen(int tm){
    
}

void safe_login(struct account *acc)
{
    printf("#-#-#-#-#-#-#-#-#\n");
    printf("Enter nickname: ");
    fgets(acc->nickname, sizeof acc->nickname, stdin);
    printf("Enter password: ");
    fgets(acc->password, sizeof acc->password, stdin);
    printf("#-#-#-#-#-#-#-#-#\n");
    
}

void sparse_cmd(char *cmd, struct account *acc){
    if(strcmp(cmd, "help\n") == 0)
    {
        printf("Available commands: help, set_nickname, shell, systeminfo, exit, clear, get_flag.\n");
    }else if(strcmp(cmd, "systeminfo\n") == 0){
        printf("All you need to know: linux x64\n");
    }else if(strcmp(cmd, "get_flag\n") == 0){
        printf("PermCTF{Yea6_h3lp_1s_G0ld}\n");
    }else if(strcmp(cmd, "exit\n") == 0){
        printf("Bye\n");
        running = 0;
    }else if(strcmp(cmd, "shell\n") == 0){
        printf("Permission denied.\n");
        running = 0;
    }else if(strcmp(cmd, "set_nickname\n") == 0){
        char nickname_shadow[24];

        clear_screen(0);
        printf("Enter new nickname: ");
        fgets(nickname_shadow, sizeof nickname_shadow, stdin);
        memset(acc->nickname, 0, 24);
        // TODO: some checks for nickname
        sprintf(acc->nickname, nickname_shadow);         //vuln
        clear_screen(1);
    }else if(strcmp(cmd, "clear\n") == 0){
        clear_screen(0);
    }

}

void prompt_loop(struct account *acc)
{
    clear_screen(2);
    while (1)
    {
        if(!running)
            break;
        char *input = (char *) malloc(32);
        printf("%s", acc->nickname);  
        printf("<- ");
        fgets(input, 32, stdin);
        sparse_cmd(input, acc);
        
    }
}

// no protections
int main(){

    setbuf(stdout, NULL);   // <----- -_-

    struct account a;
    printf("<< rmt_ctrl_v_0.1.1 >>\n");
    safe_login(&a);
    prompt_loop(&a);
    return 0; 
}

