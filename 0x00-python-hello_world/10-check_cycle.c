#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: listint_t
 *Return: If cycle then 1 -- If No cycle return 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *Current = list, *ToCheck = list;

	if (!list || !(list->next))
	{return (0); }
	for (; Current && ToCheck && ToCheck->next; )
	{
		Current = Current->next;
		ToCheck = ToCheck->next->next;
		if (Current == ToCheck)
		{
			return (1);
		}
	}
	return (0);
}
