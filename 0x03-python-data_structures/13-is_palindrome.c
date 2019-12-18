#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: listint_t
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowPTR = *head, *fastPTR = *head;
	listint_t *Node, *Previous;
	int Ans = 0;

	if (*head && (*head)->next)
	{
		for (; fastPTR && fastPTR->next; )
		{
			fastPTR = fastPTR->next->next;
			slowPTR = slowPTR->next;
		}
		Node = slowPTR;
		Previous = NULL;
		for (; Node; )
		{
			fastPTR = Node->next;
			Node->next = Previous;
			Previous = Node;
			Node = fastPTR;
		}
		fastPTR = *head;
		Node = Previous;
		for (; Previous; )
		{
			if (fastPTR->n != Previous->n)
			{
				Ans = 1;
				break;
			}
			fastPTR = fastPTR->next;
			Previous = Previous->next;
		}
		Previous = NULL;
		for (; Node; )
		{
			fastPTR = Node->next;
			Node->next = Previous;
			Previous = Node;
			Node = fastPTR;
		}
	}
	return (!Ans);
}
