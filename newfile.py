```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>পেমেন্ট ও ওয়ালেট সার্ভিস পোর্টাল</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#eef2ff',
                            100: '#e0e7ff',
                            500: '#6366f1',
                            600: '#4f46e5',
                            700: '#4338ca',
                            900: '#312e81',
                        },
                        bkash: '#e2136e',
                        nagad: '#f7931e'
                    }
                }
            }
        }
    </script>
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Hind Siliguri', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-brand-500 selection:text-white pb-10">

    <!-- নেভিগেশন বার -->
    <header class="sticky top-0 z-50 glass-card border-b border-slate-700/50 px-4 py-3">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 to-violet-500 flex items-center justify-center shadow-lg shadow-brand-500/30">
                    <i class="fa-solid fa-wallet text-white text-lg"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight">ডিজিটাল ওয়ালেট & সার্ভিস</h1>
                    <p class="text-xs text-slate-400">আপনার নিজস্ব ব্যালেন্স সেন্টার</p>
                </div>
            </div>
            
            <div class="flex items-center space-x-2">
                <!-- মোড সুইচ বাটন -->
                <button id="adminToggleBtn" onclick="toggleAdminModal()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-amber-400 border border-amber-500/30 transition flex items-center gap-1.5">
                    <i class="fa-solid fa-user-shield"></i>
                    <span>এডমিন মোড</span>
                </button>
            </div>
        </div>
    </header>

    <!-- প্রধান কন্টেইনার -->
    <main class="max-w-4xl mx-auto w-full px-4 pt-6 space-y-6">

        <!-- ইউজার আইডি আইডিয়াল অ্যাকাউন্ট কার্ড (যদি সাইন ইন না থাকে) -->
        <div id="loginCard" class="glass-card rounded-2xl p-6 shadow-xl border border-brand-500/20 text-center">
            <div class="w-16 h-16 bg-brand-500/10 text-brand-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <i class="fa-solid fa-user-plus text-2xl"></i>
            </div>
            <h2 class="text-xl font-bold mb-2">আপনার টেলিগ্রাম অ্যাকাউন্ট যুক্ত করুন</h2>
            <p class="text-slate-400 text-sm mb-6">আপনার টেলিগ্রাম User ID বা মোবাইল নাম্বার লিখে অ্যাকাউন্টে প্রবেশ করুন।</p>
            
            <div class="max-w-md mx-auto space-y-3">
                <input type="text" id="telegramUserIdInput" placeholder="যেমন: 8434665762 বা আপনার নাম" class="w-full bg-slate-800/90 border border-slate-700 rounded-xl px-4 py-3 text-white placeholder-slate-500 focus:outline-none focus:border-brand-500 transition text-center">
                <button onclick="loginUser()" class="w-full bg-gradient-to-r from-brand-600 to-violet-600 hover:from-brand-500 hover:to-violet-500 text-white font-bold py-3 px-6 rounded-xl shadow-lg shadow-brand-500/25 transition">
                    অ্যাাকাউন্টে প্রবেশ করুন
                </button>
            </div>
        </div>

        <!-- ইউজার ড্যাশবোর্ড (লগইন করার পর দেখাবে) -->
        <div id="userDashboard" class="hidden space-y-6">
            
            <!-- ওয়ালেট স্ট্যাটাস কার্ড -->
            <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-brand-900 via-indigo-900 to-slate-900 p-6 border border-brand-500/30 shadow-2xl">
                <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-brand-500/10 rounded-full blur-2xl"></div>
                
                <div class="flex justify-between items-start mb-4">
                    <div>
                        <span class="text-xs uppercase tracking-wider text-brand-300 font-semibold bg-brand-500/20 px-2.5 py-1 rounded-full border border-brand-500/30">অফিশিয়াল ওয়ালেট</span>
                        <h3 class="text-slate-300 text-sm mt-2 flex items-center gap-2">
                            <span>ইউজার ID:</span>
                            <span id="displayUserId" class="font-mono text-white font-semibold">---</span>
                        </h3>
                    </div>
                    <button onclick="logoutUser()" class="text-slate-400 hover:text-red-400 text-xs flex items-center gap-1 transition">
                        <i class="fa-solid fa-right-from-bracket"></i> লগআউট
                    </button>
                </div>

                <div class="mt-4">
                    <p class="text-xs text-slate-400">বর্তমান মোট ব্যালেন্স</p>
                    <div class="text-4xl font-extrabold text-white mt-1 flex items-baseline gap-1">
                        <span id="userBalanceDisplay">৳ 0.00</span>
                    </div>
                </div>

                <div class="mt-6 pt-4 border-t border-slate-700/50 flex flex-wrap gap-3">
                    <button onclick="openDepositModal()" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold py-2.5 px-4 rounded-xl shadow-lg transition flex items-center justify-center gap-2 text-sm">
                        <i class="fa-solid fa-plus-circle"></i> ফান্ড যোগ করুন (Deposit)
                    </button>
                    <button onclick="scrollToServices()" class="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold py-2.5 px-4 rounded-xl border border-slate-700 transition flex items-center justify-center gap-2 text-sm">
                        <i class="fa-solid fa-cube"></i> সার্ভিসসমূহ দেখুন
                    </button>
                </div>
            </div>

            <!-- সার্ভিস শপ সেকশন -->
            <div id="servicesStore" class="space-y-4">
                <div class="flex items-center justify-between">
                    <h2 class="text-lg font-bold flex items-center gap-2">
                        <i class="fa-solid fa-store text-brand-500"></i>
                        <span>আমাদের প্রিমিয়াম সার্ভিসসমূহ</span>
                    </h2>
                    <span class="text-xs text-slate-400">ব্যালেন্স দিয়ে সরাসরি অর্ডার করুন</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" id="servicesGrid">
                    <!-- JavaScript dynamically injects services here -->
                </div>
            </div>

            <!-- ইউজার ট্রানজেকশন হিস্ট্রি -->
            <div class="glass-card rounded-2xl p-5 border border-slate-700/60">
                <h3 class="text-md font-bold mb-3 flex items-center gap-2">
                    <i class="fa-solid fa-clock-rotate-left text-brand-400"></i>
                    <span>পেমেন্ট ও ডিপোজিট হিস্ট্রি</span>
                </h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="bg-slate-800/80 text-xs uppercase text-slate-400 border-b border-slate-700">
                            <tr>
                                <th class="p-3">তারিখ</th>
                                <th class="p-3">পদ্ধতি</th>
                                <th class="p-3">অ্যামাউন্ট</th>
                                <th class="p-3">TrxID</th>
                                <th class="p-3">স্ট্যাটাস</th>
                            </tr>
                        </thead>
                        <tbody id="userHistoryTable">
                            <!-- JS Dynamically populated -->
                        </tbody>
                    </table>
                </div>
            </div>

        </div>

        <!-- এডমিন ড্যাশবোর্ড (পাসওয়ার্ড সুরক্ষিত) -->
        <div id="adminDashboard" class="hidden space-y-6">
            <div class="bg-amber-500/10 border border-amber-500/30 rounded-2xl p-4 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center">
                        <i class="fa-solid fa-user-shield text-xl"></i>
                    </div>
                    <div>
                        <h2 class="font-bold text-amber-300">এডমিন কন্ট্রোল প্যানেল</h2>
                        <p class="text-xs text-amber-200/70">ইউজার পেমেন্ট এপ্রুভ করুন এবং ব্যালেন্স যুক্ত করুন</p>
                    </div>
                </div>
                <button onclick="closeAdminMode()" class="bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs px-3 py-2 rounded-lg transition border border-slate-700">
                    ইউজার ভিউতে যান
                </button>
            </div>

            <!-- এডমিন পেন্ডিং পেমেন্ট লিস্ট -->
            <div class="glass-card rounded-2xl p-5 border border-amber-500/20">
                <h3 class="text-md font-bold mb-4 flex items-center justify-between">
                    <span class="flex items-center gap-2">
                        <i class="fa-solid fa-bell text-amber-400"></i> পেন্ডিং পেমেন্ট রিকোয়েস্ট
                    </span>
                    <span id="pendingBadge" class="bg-amber-500/20 text-amber-300 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-amber-500/30">0 টি পেন্ডিং</span>
                </h3>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="bg-slate-800/90 text-xs uppercase text-slate-400 border-b border-slate-700">
                            <tr>
                                <th class="p-3">ইউজার ID</th>
                                <th class="p-3">মেথড</th>
                                <th class="p-3">টাকার পরিমাণ</th>
                                <th class="p-3">TrxID</th>
                                <th class="p-3 text-right">অ্যাকশন</th>
                            </tr>
                        </thead>
                        <tbody id="adminPendingTable">
                            <!-- JS Inject Pending Requests -->
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- সরাসরি যেকোনো ইউজারের ব্যালেন্স পরিবর্তন এডমিন টুল -->
            <div class="glass-card rounded-2xl p-5 border border-slate-700">
                <h3 class="text-md font-bold mb-4 flex items-center gap-2 text-brand-300">
                    <i class="fa-solid fa-coins"></i> ইউজার ব্যালেন্স কাস্টম এডিটর (Custom Balance)
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">ইউজার ID টাইপ করুন</label>
                        <input type="text" id="adminTargetUserId" placeholder="যেমন: 8434665762" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">অ্যামাউন্ট (টাকা)</label>
                        <input type="number" id="adminCustomAmount" placeholder="যেমন: 500" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500">
                    </div>
                    <div class="flex items-end gap-2">
                        <button onclick="adminAdjustBalance('add')" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold py-2 px-3 rounded-xl text-sm transition">
                            + যোগ করুন
                        </button>
                        <button onclick="adminAdjustBalance('set')" class="flex-1 bg-brand-600 hover:bg-brand-500 text-white font-semibold py-2 px-3 rounded-xl text-sm transition">
                            সেট করুন
                        </button>
                    </div>
                </div>
            </div>

            <!-- সকল রেজিস্টার্ড ইউজারের তালিকা -->
            <div class="glass-card rounded-2xl p-5 border border-slate-700">
                <h3 class="text-md font-bold mb-3 flex items-center gap-2">
                    <i class="fa-solid fa-users text-slate-400"></i> সকল ইউজার অ্যাকাউন্ট সমূহের তালিকা
                </h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-300">
                        <thead class="bg-slate-800 text-xs uppercase text-slate-400 border-b border-slate-700">
                            <tr>
                                <th class="p-3">ইউজার ID</th>
                                <th class="p-3">বর্তমান ব্যালেন্স</th>
                                <th class="p-3">মোট ডিপোজিট</th>
                                <th class="p-3">অ্যাকশন</th>
                            </tr>
                        </thead>
                        <tbody id="adminAllUsersTable">
                            <!-- JS Inject All Users -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </main>

    <!-- ডিপোজিট মডাল (ইউজারের জন্য) -->
    <div id="depositModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="glass-card rounded-2xl max-w-md w-full p-6 relative border border-slate-700 shadow-2xl">
            <button onclick="closeDepositModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white">
                <i class="fa-solid fa-xmark text-xl"></i>
            </button>
            <h3 class="text-lg font-bold mb-1 flex items-center gap-2">
                <i class="fa-solid fa-wallet text-emerald-400"></i> ডিপোজিট ফরম
            </h3>
            <p class="text-xs text-slate-400 mb-4">নিচের যেকোনো বিকাশ/নগদ নম্বরে টাকা পাঠাইয়া রিকোয়েস্ট সাবমিট করুন।</p>

            <div class="bg-slate-800/80 p-3 rounded-xl mb-4 border border-slate-700 text-xs space-y-1.5">
                <p class="flex justify-between items-center">
                    <span class="text-bkash font-bold flex items-center gap-1"><i class="fa-solid fa-mobile-screen"></i> বিকাশ Personal:</span>
                    <span class="font-mono bg-slate-900 px-2 py-0.5 rounded text-white font-bold select-all">01953192653</span>
                </p>
                <p class="flex justify-between items-center">
                    <span class="text-nagad font-bold flex items-center gap-1"><i class="fa-solid fa-mobile-screen"></i> নগদ Personal:</span>
                    <span class="font-mono bg-slate-900 px-2 py-0.5 rounded text-white font-bold select-all">01953192653</span>
                </p>
            </div>

            <form onsubmit="submitDeposit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs text-slate-400 mb-1">পেমেন্ট মেথড বাছাই করুন</label>
                    <select id="depMethod" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:outline-none focus:border-brand-500">
                        <option value="bKash">বিকাশ (bKash Send Money)</option>
                        <option value="Nagad">নগদ (Nagad Send Money)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs text-slate-400 mb-1">কত টাকা পাঠিয়েছেন (টাকার পরিমাণ)</label>
                    <input type="number" id="depAmount" min="10" required placeholder="যেমন: 100, 500" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:outline-none focus:border-brand-500">
                </div>
                <div>
                    <label class="block text-xs text-slate-400 mb-1">TrxID (ট্রানজেকশন আইডি)</label>
                    <input type="text" id="depTrxId" required placeholder="যেমন: BLA9X8K2M" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:outline-none focus:border-brand-500">
                </div>
                <button type="submit" class="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-emerald-600/20">
                    ডিপোজিট রিকোয়েস্ট পাঠান
                </button>
            </form>
        </div>
    </div>

    <!-- এডমিন পিন ভেরিফিকেশন মডাল -->
    <div id="adminPinModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="glass-card rounded-2xl max-w-xs w-full p-6 text-center border border-amber-500/30">
            <div class="w-12 h-12 bg-amber-500/20 text-amber-400 rounded-full flex items-center justify-center mx-auto mb-3">
                <i class="fa-solid fa-lock text-xl"></i>
            </div>
            <h3 class="font-bold text-lg mb-1">এডমিন পিন টাইপ করুন</h3>
            <p class="text-xs text-slate-400 mb-4">ডিফল্ট পিন পাসওয়ার্ড: <span class="text-amber-300 font-mono font-bold">1234</span></p>

            <input type="password" id="adminPinInput" placeholder="PIN" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-center text-lg font-mono tracking-widest mb-4 focus:outline-none focus:border-amber-500">

            <div class="flex gap-2">
                <button onclick="closeAdminPinModal()" class="flex-1 bg-slate-800 text-slate-300 py-2 rounded-xl text-sm">বাতিল</button>
                <button onclick="verifyAdminPin()" class="flex-1 bg-amber-600 hover:bg-amber-500 text-white font-bold py-2 rounded-xl text-sm">প্রবেশ</button>
            </div>
        </div>
    </div>

    <!-- নোটিফিকেশন টোস্ট -->
    <div id="toast" class="fixed bottom-5 right-5 z-50 hidden max-w-sm glass-card px-4 py-3 rounded-xl border border-brand-500/40 shadow-xl flex items-center space-x-3 transition">
        <i id="toastIcon" class="fa-solid fa-circle-check text-emerald-400 text-lg"></i>
        <p id="toastMessage" class="text-sm font-medium text-slate-200">সফল হয়েছে!</p>
    </div>

    <script>
        // ------------------ ডাটাবেজ স্টেট (Local Storage Based) ------------------
        let currentUser = localStorage.getItem('active_tg_user') || null;
        
        // ডিফল্ট ডেমো ইউজার ডাটাবেজ
        let usersData = JSON.parse(localStorage.getItem('portal_users')) || {
            '8434665762': { balance: 500, totalDeposit: 500 },
            '123456789': { balance: 120, totalDeposit: 200 }
        };

        // সার্ভিস শপ ক্যাটালগ
        let availableServices = [
            { id: 1, name: 'প্রিমিয়াম ভিআইপি এক্সেস (১ মাস)', price: 100, icon: 'fa-crown', color: 'from-amber-500 to-orange-600' },
            { id: 2, name: 'আল্ট্রা ফাস্ট বট বুস্টার প্যাফ', price: 250, icon: 'fa-bolt', color: 'from-brand-500 to-indigo-600' },
            { id: 3, name: '২৪/৭ স্পেশাল সাপোর্ট প্রিমিয়াম', price: 50, 