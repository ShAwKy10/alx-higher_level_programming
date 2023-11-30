#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks is list is cyclical
 * @list: pointer to list to check
 *
 * Return: 1 if cyclical, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fll = list;
	listint_t *sll = list;

	while (fll && fll->next)
	{
		sll = sll->next;
		fll = fll->next->next;
		if (sll == fll)
			return (1);
	}
	return (0);
}
