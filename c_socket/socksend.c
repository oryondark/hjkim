// 헤더파일 정의//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
//tcp/ip 헤더파일
#include <linux/ip.h>
#include <linux/tcp.h>

int main()
{
   unsigned char packet[40]; /*TCP와 IP 헤더는 각각 20바이트*/
   int SS; /* 소켓 파일 디스크립터 */
   int BUF = 1; /* 소켓 버퍼 */
   struct iphdr *iphdr;  /* ip 헤더 구조체 선언 */
   struct tcphdr *tcphdr; /* tcp 헤더 구조체 선언 */
   struct sockaddr_in address; /* IP 4버전이 사용하는 구조체계 */
   
SS = socket( AF_INET, SOCK_RAW, IPPROTO_RAW ); 

setsockopt( SS, IPPROTO_IP, IP_HDRINCL, (char *)&BUF, sizeof(BUF));
/* 위 소켓 옵션 지정 */

// TCP HEAER 설정 
tcphdr = (struct tcphdr *)(packet + 20); 
/* 위 함수의 저런 형식의 설정 의미는 TCP/IP 통신에서 가장 먼저 오는 헤더는 IP헤더다.
 * 따라서, 위 지정 방식은 tcp 영역 전 ip 영역 20바이트를 설정해 둔 것을 의미한다. */

memset((char *)tcphdr, 0, 20); /* 메모리 초기화 */
tcphdr -> source = htons( 5450 ); /* 송신 포트 */
tcphdr -> dest = htonl( 3300 ); /* 수신자 포트 */
tcphdr -> seq = htonl(7666501);
tcphdr -> ack_seq = htonl(3433341);
tcphdr -> doff = 5;
tcphdr -> syn = 1; /* SYN 플래그 설정 */
tcphdr -> window = htons(512); /* 수신창 설정 */
tcphdr -> check = 1;

//IP HEADER 설정

iphdr = (struct iphdr *)packet;

iphdr -> version = 4; /* ip 버전 */
iphdr -> ihl = 5; /* IP header 길이 "5" */
iphdr -> protocol = IPPROTO_TCP;
iphdr -> tot_len = 40; /* 패킷의 총 길이 40 */
iphdr -> id = htons( 1010 ); /* 각각의 패킷을 구분할 때 쓰이는 ID 값으로 임의로 지정 */
iphdr -> ttl = 70; /* Time To Live */
iphdr -> check = 1; 
iphdr -> saddr = inet_addr("123.123.123.123"); /* 발신 주소 */
iphdr -> daddr = inet_addr("172.30.1.1"); /* 수신 IP 주소 */

/* sendto 함수에서 사용될 패킷을 전송하기 위한 설정 값 */
address.sin_family = AF_INET;
address.sin_port = htons ( 3300 );
address.sin_addr.s_addr = ("172.30.1.1"); 

sendto( SS, &packet, sizeof(packet), 0x0, (struct sockaddr *)&address, sizeof(address));
}












 



   

