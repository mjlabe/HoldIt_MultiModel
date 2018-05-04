#Views

The views are divided up by groups so that:
* Only logged in users can view restricted pages
* Each group has its own **privileges** as well as the **privileges** of the group below
* Only users in the corresponding group can view that group's views/pages (and the views/pages with lower privilege)
* The **hierarchy privilege** is in the following order (highest privilege to lowest), with details below:
    1) Admin
    2) Contributor
    3) User
    4) Public


##Public Views

These views are visible to **anyone**, regardless of what group they belong to. Be sure to limit the pages in this view
since it is a **security risk**.

The following views belong to **views_public**:

* login
* logout
* signup
* index

Since **index** (our homepage) is **public**, be sure to limit what information is on the page. Also, think carefully
about adding more views to **views_public**, we want to limit access to the content and keep it **secure**.


##User Views

These views are limited to users that only have **read privileges**.


##Contributors Views

These views are limited to users that have **read privileges** and **limited write privileges**.

Right now, the following code is used to limit access to to **views_contrib**:

<pre><code>def is_contributor(user):
    return user.groups.filter(name='Contributor').exists()
 
@user_passes_test(is_contributor)   #decorator
</code></pre>

A better implementation would include custom **Middleware** to limit access to **all** pages by default. That way, if
a view or page didn't have the the above (or corresponding **decorator**), the page/view would not be accessible. 

The following views belong to **views_contrib**:

* new_report


##Admin Views

User with **admin** privileges can view any page/view and have their own pages for administrative tasks.

