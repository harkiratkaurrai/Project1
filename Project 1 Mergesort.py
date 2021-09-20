#!/usr/bin/env python
# coding: utf-8

# In[44]:


def mergesort(list1):
#Condition pour diviser la liste 
    if len(list1)>1:  #Je divise seulement si la liste a plus d'elemts que 1 
        middle = len(list1)//2 #divise la liste en 2 
        left_sublist=list1[:middle] # prend les elemensts de gauche 
        right_sublist=list1[middle:] #prend les elements de droite 
        mergesort(left_sublist)#diviser encore gauche 
        mergesort(right_sublist)#diviser encore droite 
        i=0 #index de left_list
        j=0
        k=0    
#comparer les valeurs dans la liste a gauche avec les valeurs dans la liste de droite
#Mettre les index a 0 pour right_list , left_list, list1
#Faut comparer ces valeurs plusieurs fois donc on peut utiliser la boucle while
#Condition pour rassembler les elements 
        while i<len(left_sublist) and j<len(right_sublist):#Index doit etre plus petit que la longeur de la liste 
            if left_sublist[i]<right_sublist[j]:# si l'element de gauche est infereur a l'elemt de droite 
                list1[k]=left_sublist[i]# si inferieur mettre dans la liste d'origine list1
                i=i+1 #incrementer l'index a chaque fois de la liste gauche
                k=k+1
            else:
                list1[k]=right_sublist[j]# si la valeur dans la liste de droite est plus petite mettre dans la liste 1
                j=j+1
                k=k+1
#faut ecrire une condition pour le dernier element qui se trouve seul 
#Condition pour verifier s'il ya un elemt manquant ou pas 
        while i<len(left_sublist):#S'il y a un elemt restant dans la liste de gauche 
            list1[k]=left_sublist[i]
            i=i+1            
            k=k+1
        while j<len(right_sublist):#s'il ya un elemt restant dans la liste de droite 
            list1[k]=right_sublist[j]
            j=j+1
            k=k+1


# In[45]:


#Ecrire le numero d'elemets
number=int(input("write the number of elents :"))


# In[ ]:


list1 =[int(input()) for x in range(number)]


# In[43]:


mergesort(list1)
print("sorted list is:",list1)


# In[ ]:





# In[ ]:




