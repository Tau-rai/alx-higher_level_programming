#include "lists.h"

int is_palindrome(listint_t **head);
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to a linked list
 * Return: Always 0 Success.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;
	listint_t *mid = NULL;
	int flag = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	next = slow;
	prev->next = NULL;
	/* reverse the half of the list*/
	while (next != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	mid = (mid == NULL) ? prev : mid;

	listint_t *f_half = *head;
	listint_t *sec_half = mid;

	while (f_half != NULL && sec_half != NULL)
	{
		if (f_half->n != sec_half->n)
		{
			flag = 0;
			break;
		}
		f_half = f_half->next;
		sec_half = sec_half->next;
	}

	/* restore the orig list */
	prev = NULL;
	while (mid != NULL)
	{
		next = mid->next;
		mid->next = prev;
		prev = mid;
		mid = next;
	}
	prev = NULL;
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	return (flag);
}
