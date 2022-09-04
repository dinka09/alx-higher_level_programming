#include "lists.h"
/**
 * palindrome - check if palindrome with recuursion
 * @l: l
 * @r: r
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **l, listint_t *r)
{
	int response;

	if (r != NULL)
	{
		response = palindrome(1, r->next);
		if (response != 0)
		{
			response = (r->n == (*1)->n);
			*1 = (*1)->next;
			return (response);
		}
		return (0);
	}
	return (1);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}


