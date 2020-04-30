#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
/*
* 14931480 KIMHYUNJUNE
*/


typedef struct student{
	char name[250];
	//char cls[50];
	//char lang_art[50];
	//char english[50];
	//char math[50];
	struct student *n_st;
	
}student;

typedef struct student *st;

typedef struct _collect{
	
	int idx;
	st *next;

}collect;

void setStudentInfo(struct student **prv_st);
void print_total_st_score(struct student **prv_st);
