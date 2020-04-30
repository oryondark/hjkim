
#include "score.h"


int main(int argc, char **argv){
	printf("14931480 KIMHYUNJUNE\n");
	/*
	* this programe used linked list.
	* 14931480 by HJ
	* start project day = 2017.11.25
	* finish project day = 2017.11.25
	*/
	student *head_st = NULL;
	head_st = (student *)malloc(sizeof(student));
	int processing = 1;
	setStudentInfo(head_st);
	/*
	printf("%s\n", head_st->name);
	printf("%s\n", head_st->cls);
	printf("%s\n", head_st->lang_art);
	printf("%s\n", head_st->english);
	printf("%s\n", head_st->math);
	*/
	while(processing != 0){
		printf("Is there anything more data ?[y/n]\n");

		char YN[10];
		char y[] = "y";
		char n[] = "n";
		gets(YN);

		if(strcmp(YN,y) == 0){
			setStudentInfo(head_st);
		}
		if(strcmp(YN,n) == 0){
			break;
		}
	}

	print_total_st_score(head_st);
	free(head_st);

}

void print_total_st_score(struct student **prv_st){
	student *ptr_st = NULL;
	ptr_st = *prv_st;

	printf("  name  |  class  |  language  |  english  |  math  |\n");
	printf("-----------------------------------------------------\n");


	while(ptr_st != NULL){

		printf("%s\n", ptr_st->name);
		ptr_st = ptr_st->n_st;
	}
	return;
}

void setStudentInfo(struct student **prv_st){
	char name[20];
	char cls[20];
	char lang_art[20];
	char english[20];
	char math[20];


	char buf[249];

	student *new_st = NULL;
	new_st = (student *)malloc(sizeof(student));
	student *ptr_st = NULL;
	ptr_st = *prv_st;

	printf("input name \n");
	gets(name);
	printf("input class \n");
	gets(cls);
	printf("nation language \n");
	gets(lang_art);
	printf("english \n");
	gets(english);
	printf("input math score \n");
	gets(math);

	sprintf(buf, " %s | %d | %d | %d | %d |", name,atoi(cls),atoi(lang_art),atoi(english),atoi(math));

	memcpy(new_st->name, buf, sizeof(buf) + 1);

	new_st->n_st = NULL;
	if(*prv_st == NULL){
		*prv_st = new_st;
		return;
	}
	while(ptr_st->n_st != NULL){
		ptr_st = ptr_st->n_st;
	}
	ptr_st->n_st = new_st;
	printf("Done.\n");
	return;
}
