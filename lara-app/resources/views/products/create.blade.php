<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Create the product</h1>
    <div>
        @if($errors->any())
        <ul>
            @foreach($errors->all() as $err)
                <li>{{$err}}</li>
            @endforeach
        </ul>
        @endif
    </div>
    <form action="{{route('product.store')}}" method="post">
        @csrf
        @method('post')
        <div>
            <label for="name">Name</label>
            <input type="text" name="name" id="name"  >
        </div>
        <div>
            <label for="qty">Quantity</label>
            <input type="text" name="qty" id="qty" >
        </div>
        <div>
            <label for="price">Price</label>
            <input type="text" name="price" id="price"  >
        </div>
        <div>
            <label for="description">Description</label>
            <input type="text" name="description" id="description"  >
        </div>
        <div>
            <input type="submit" value="save a new Product">
        </div>
    </form>
</body>
</html>