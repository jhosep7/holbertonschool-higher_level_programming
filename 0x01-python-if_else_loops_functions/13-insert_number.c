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

	if (*head == NULL)
	{
		*head = NewNode;
		NewNode->next = NULL;
		return (NewNode);
	}
	Tcurrent = *head;
	while (Tcurrent != NULL)
	{
		if (Tcurrent->n > number)
		{
			NewNode->next = Tcurrent;
			*head = NewNode;
			return (NewNode);
		}
		if (Tcurrent->next->n >= number)
		{
			NewNode->next = Tcurrent->next;
			Tcurrent->next = NewNode;
			return (NewNode);
		}
		Tcurrent = Tcurrent->next;
	}
	NewNode->next = NULL;
	Tcurrent->next = NewNode;
	return(NewNode);
}
