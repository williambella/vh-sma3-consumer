async function loadUser(id) {
  const r = await fetch(`/api/v1/users/${id}`);
  return r.json();
}
