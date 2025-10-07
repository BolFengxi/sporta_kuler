function showToast(title, message, type = "info") {
  const toast = document.getElementById("toast-component");
  const icon = document.getElementById("toast-icon");
  const progressBar = document.querySelector("#toast-progress div");
  const close = document.getElementById("toast-close");
  const titleEl = document.getElementById("toast-title");
  const messageEl = document.getElementById("toast-message");

  // Mapping ikon dan warna pastel
  const icons = {
    success: "✔️",
    error: "❌",
    warning: "⚠️",
    info: "ℹ️",
  };

  const bgColors = {
    success: "bg-green-100 border-green-300",
    error: "bg-red-100 border-red-300",
    warning: "bg-yellow-100 border-yellow-300",
    info: "bg-blue-100 border-blue-300",
  };

  const iconColors = {
    success: "bg-green-500",
    error: "bg-red-500",
    warning: "bg-yellow-500",
    info: "bg-blue-500",
  };

  // Reset semua kelas
  toast.className = `
    fixed bottom-8 right-8 p-5 min-w-[280px] max-w-sm rounded-2xl shadow-2xl z-50
    opacity-0 pointer-events-none translate-y-5 scale-95 transition-all duration-500 ease-out
    flex items-start gap-4 border
  `;

  // Tambahkan warna sesuai tipe
  toast.classList.add(...bgColors[type].split(" "));

  // Update konten
  icon.innerHTML = `
    <div class="flex items-center justify-center w-8 h-8 rounded-full text-white ${iconColors[type]}">
      ${icons[type] || "💬"}
    </div>
  `;
  titleEl.textContent = title;
  messageEl.textContent = message;

  // Reset progress bar
  progressBar.className = "h-full bg-gradient-to-r from-[#42A5F5] to-[#1E88E5] w-0 transition-all duration-[3000ms]";

  // Munculkan toast
  setTimeout(() => {
    toast.classList.remove("opacity-0", "translate-y-5", "pointer-events-none", "scale-95");
    toast.classList.add("opacity-100", "translate-y-0", "scale-100", "pointer-events-auto");
    progressBar.classList.add("w-full");
  }, 50);

  // Fungsi untuk menyembunyikan toast
  const hide = () => {
    toast.classList.remove("opacity-100", "translate-y-0", "scale-100");
    toast.classList.add("opacity-0", "translate-y-5", "scale-95", "pointer-events-none");
    setTimeout(() => (progressBar.classList.remove("w-full")), 500);
  };

  // Tutup otomatis setelah 3 detik
  setTimeout(hide, 3000);
  close.onclick = hide;
}
