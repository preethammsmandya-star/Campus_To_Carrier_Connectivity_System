import os
import re

replacements = {
    r'\btext-slate-800\b': 'text-white',
    r'\btext-slate-500\b': 'text-slate-400',
    r'\bbg-white/60\b': 'bg-slate-800/30',
    r'\bbg-white\b': 'bg-slate-800',
    r'\bbg-slate-50\b': 'bg-slate-900',
    r'\bborder-slate-200\b': 'border-slate-700/50',
    r'\bbg-slate-200\b': 'bg-slate-700',
    r'\btext-slate-600\b': 'text-slate-300',
}

def process():
    for root, _, files in os.walk('frontend/src/pages'):
        for file in files:
            if file.endswith('.jsx'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Protect hero banners
                hero_pattern = re.compile(r'(<div className="relative rounded-2xl overflow-hidden mb-8".*?<!-- HERO END -->|relative z-10 p-8 md:p-12 h-full.*?</p>)', re.DOTALL)
                
                def protect(match):
                    return match.group(0).replace('text-slate-800', 'TEXT_SLATE_800_PROTECTED').replace('text-slate-500', 'TEXT_SLATE_500_PROTECTED')
                
                content = hero_pattern.sub(protect, content)
                
                # Replace classes
                for old, new in replacements.items():
                    content = re.sub(old, new, content)
                    
                # Restore
                content = content.replace('TEXT_SLATE_800_PROTECTED', 'text-slate-800').replace('TEXT_SLATE_500_PROTECTED', 'text-slate-500')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    process()
