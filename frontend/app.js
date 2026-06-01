const apiBase = "http://localhost:5000/api";

document.addEventListener("DOMContentLoaded", () => {
  const ingredientsInput = document.getElementById("ingredients-input");
  const getRecipesBtn = document.getElementById("get-recipes-btn");
  const recipesList = document.getElementById("recipes-list");
  const favoritesList = document.getElementById("favorites-list");
  const refreshFavoritesBtn = document.getElementById("refresh-favorites-btn");

  getRecipesBtn.addEventListener("click", async () => {
    const raw = ingredientsInput.value.trim();
    if (!raw) {
      alert("Please enter some ingredients.");
      return;
    }
    const ingredients = raw.split(",").map(s => s.trim()).filter(Boolean);
    recipesList.innerHTML = "Loading...";

    try {
      const res = await fetch(`${apiBase}/recipes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ingredients })
      });
      const data = await res.json();
      renderRecipes(data.recipes || []);
    } catch (err) {
      console.error(err);
      recipesList.innerHTML = "Error fetching recipes.";
    }
  });

  refreshFavoritesBtn.addEventListener("click", loadFavorites);

  async function loadFavorites() {
    favoritesList.innerHTML = "Loading...";
    try {
      const res = await fetch(`${apiBase}/favorites`);
      const data = await res.json();
      renderFavorites(data.favorites || []);
    } catch (err) {
      console.error(err);
      favoritesList.innerHTML = "Error loading favorites.";
    }
  }

  function renderRecipes(recipes) {
    if (!recipes.length) {
      recipesList.innerHTML = "No recipes found.";
      return;
    }
    recipesList.innerHTML = "";
    recipes.forEach(recipe => {
      const div = document.createElement("div");
      div.className = "recipe";

      const title = document.createElement("div");
      title.className = "recipe-title";
      title.textContent = recipe.title;

      const ing = document.createElement("div");
      ing.className = "small-text";
      ing.textContent = "Ingredients: " + (recipe.ingredients || []).join(", ");

      const instr = document.createElement("div");
      instr.textContent = recipe.instructions || "";

      const saveBtn = document.createElement("button");
      saveBtn.textContent = "Save to favorites";
      saveBtn.addEventListener("click", () => saveFavorite(recipe));

      div.appendChild(title);
      div.appendChild(ing);
      div.appendChild(instr);
      div.appendChild(saveBtn);

      recipesList.appendChild(div);
    });
  }

  function renderFavorites(favorites) {
    if (!favorites.length) {
      favoritesList.innerHTML = "No favorites yet.";
      return;
    }
    favoritesList.innerHTML = "";
    favorites.forEach(fav => {
      const div = document.createElement("div");
      div.className = "favorite";

      const title = document.createElement("div");
      title.className = "favorite-title";
      title.textContent = fav.title;

      const ing = document.createElement("div");
      ing.className = "small-text";
      ing.textContent = "Ingredients: " + (fav.ingredients || []).join(", ");

      const instr = document.createElement("div");
      instr.textContent = fav.instructions || "";

      const delBtn = document.createElement("button");
      delBtn.textContent = "Delete";
      delBtn.addEventListener("click", () => deleteFavorite(fav._id));

      div.appendChild(title);
      div.appendChild(ing);
      div.appendChild(instr);
      div.appendChild(delBtn);

      favoritesList.appendChild(div);
    });
  }

  async function saveFavorite(recipe) {
    try {
      await fetch(`${apiBase}/favorites`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: recipe.title,
          ingredients: recipe.ingredients || [],
          instructions: recipe.instructions || ""
        })
      });
      await loadFavorites();
    } catch (err) {
      console.error(err);
      alert("Error saving favorite.");
    }
  }

  async function deleteFavorite(id) {
    if (!confirm("Delete this favorite?")) return;
    try {
      await fetch(`${apiBase}/favorites/${id}`, {
        method: "DELETE"
      });
      await loadFavorites();
    } catch (err) {
      console.error(err);
      alert("Error deleting favorite.");
    }
  }

  loadFavorites();
});