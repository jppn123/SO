#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define TAM 50

int main(int argc, char *argv[]) {
  //declaração das variáveis
  pid_t pid;
  int st_pai, st_filho, i;
  char *args[TAM], command[TAM], *splitCommand, dir[TAM];

  do {
    //enfeitando a entrada do bash com o diretorio atual do user
    sleep(1);
    printf("sh %s> ", getcwd(dir, TAM));
    fgets(command, TAM, stdin);

    //se o usuario digitar algum comando ele continua, se não, volta ao inicio
    if (strlen(command) == 1) {
      args[0] = "";
    } else {

      //aqui o comando digitado é dividido em um vetor para cada espaço que tiver
      splitCommand = strtok(command, " \n");

      //cada elemento do comando é insertado dentro de uma lista
      for (i = 0; splitCommand != NULL; i++) {
        args[i] = splitCommand;
        splitCommand = strtok(NULL, " \n");
      }

      //final da lista setado para null, para evitar possiveis complicações
      args[i] = NULL;

      //criação do processo filho que irá executar os comandos
      if (!(pid = fork())) {

        st_filho = execvp(args[0], args);
        //caso o comando não seja aceito pela lib do exec, irá gerar um erro
        if (st_filho == -1 && strcmp(args[0], "exit") &&
            strcmp(args[0], "cd")) {
          printf("Command '%s' not found\n", args[0]);
        }
        return 0;
      }
      //processo pai espera o filho terminar evitando processos zumbis
      waitpid(pid, &st_pai, WUNTRACED);
      
      /*
      se o comando for cd, o pai deve fazer a mudança de diretório,
      então será possivel dos filhos executarem os devidos comandos 
      no diretório informado
      */
      if (!strcmp(args[0], "cd") && (args[1] == NULL)) {
        printf("%s\n", getcwd(dir, TAM));
      } else if (!strcmp(args[0], "cd") && chdir(args[1]) == -1) {
        printf("Directory not found\n");
      }
    }
  //loop esperando o usuário cancelar o console ou o comando exit ser executado
  } while (strcmp(args[0], "exit"));
  
  printf("Exit status: %d\n", WEXITSTATUS(st_pai));
  return 0;
}
