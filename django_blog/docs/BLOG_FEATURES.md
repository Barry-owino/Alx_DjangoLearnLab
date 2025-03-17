## Blog Post Management

### Features
- Public viewing of all posts
- Authenticated users can create posts
- Authors can edit/delete their posts
- Paginated post listing (5 posts/page)

### Permission Matrix
| Action       | Authenticated | Author Required |
|--------------|---------------|-----------------|
| View list    | No            | No              |
| View detail  | No            | No              |
| Create post  | Yes           | No              |
| Edit post    | Yes           | Yes             |
| Delete post  | Yes           | Yes             |

### API Endpoints
| URL Pattern          | View Class      | Template           |
|----------------------|-----------------|--------------------|
| /post/              | PostListView    | post_list.html     |
| /post/new/          | PostCreateView  | post_form.html     |
| /post/<pk>/         | PostDetailView  | post_detail.html   |
| /post/<pk>/edit/    | PostUpdateView  | post_form.html     |
| /posts<pk>/delete/  | PostDeleteView  | post_confirm_delete|
