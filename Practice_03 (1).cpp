#include <stdio.h>

int main()
{
	int iPnum = 0 ;		// �� ������ ��� ����.
	int count = 0;			// �Ҽ��� ����

	for(int i = 2 ; i<=100 ; i++) {  // 1 ~ 100���� ���� ���� (1�� �Ҽ��� �ƴϹǷ� ����)
		for(int j = 1 ; j<=i ; j++) {		// 1��° for������ ���� ���ں��� ���� ������ �������� ����� ������ �ľ�.
			if(i%j==0) {		// �� ������ ����� ���� �ľ� ( ���� �������� ���� �ִ°�? )
				iPnum++;		// ���� �������� ���� ������ iPnum �� ����. (��� �� ���� ����)
			}
		}
		if(iPnum==2) {  // ����� ������ 2���� ���� = �Ҽ�
			count++;			// �Ҽ��� ���� ������Ŵ. �������� ������ �� = �Ҽ��� �� ����.
			printf("%d\n",i);  // �Ҽ� ���.
		}
		iPnum=0;	// 1��° for�� ������ ��� ���� �ʱ�ȭ.
	}

	printf("�Ҽ��� ���� : %d\n",count); // �Ҽ��� �� ���� ���.

	return 0;
}