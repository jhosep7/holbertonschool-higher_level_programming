#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Node head
 * @number: int
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *NewNode, *Tcurrent;

	NewNode = malloc(sizeof(listint_t));
	if (head == NULL || NewNode == NULL)
	{return (NULL); }
	NewNode->n = number;
	NewNode->next = NULL;

	Tcurrent = *head;
	while (Tcurrent != NULL)
	{
		if (!Tcurrent->next || NewNode->n < Tcurrent->next->n)
		{
			NewNode->next = Tcurrent->next;
			Tcurrent->next = NewNode;
		}
		Tcurrent = Tcurrent->next;
	}
	return (NULL);
}
