#include "lists.h"

/**
 * insert_node - insert a new node number in a sorted linked list
 * @head: pointer to the head node
 * @n: an integer value
 * Return: pointer to a new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur_node = *head;
	listint_t *n_node = malloc(sizeof(listint_t));

	if (n_node == NULL)
		return (NULL);

	n_node->n = number;
	n_node->next = NULL;

	if (!*head || (*head)->n >= number)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}

	while(cur_node->next && cur_node->next->n < number)
		cur_node = cur_node->next;

	n_node->next = cur_node->next;
	cur_node->next = n_node;

	return (n_node);
}

