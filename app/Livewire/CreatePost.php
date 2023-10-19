<?php

namespace App\Livewire;

use Livewire\Component;
use App\Models\Post;

class CreatePost extends Component
{
    public $title = "learning livewire";

    public function save()
    {
        $post = Post::create([
            'title' => $this->title,
        ]);

        return redirect()->to('posts')->with('status', 'Post Created');
    }

    public function render()
    {
        return view('livewire.create-post')->with([
            'name' => 'Bilal',
        ]);
    }
}
