#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: O if theres no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *fast = list->next;

	if (!list)
		return (0);

	while (head != NULL && fast != NULL && fast->next != NULL)
	{
		if (head == fast)
			return (1);

		head = head->next;
		fast = fast->next->next;
	}

	return (0);
}
